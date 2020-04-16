from django.db import models

# Create your models here.
import datetime
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin )
from django.utils.translation import gettext_lazy as _
import PIL

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=200, default="Ivan")
    surname = models.CharField(max_length=200, default="Petrov")
    is_doe = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_prof = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Group(models.Model):
    group = models.CharField(max_length=200, default="BS18-03")


class Student(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True)
    # track is also part of a direction
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    graduation_year = models.IntegerField()


class DoeMember(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True)
    photo = models.ImageField(default=None, upload_to='database_pictures')


class Professor(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True)
    photo = models.ImageField(default=None, upload_to='database_pictures')


class Course(models.Model):
    title = models.CharField(max_length=200)
    # to mark the semester
    description = models.CharField(max_length=1000)
    is_elective = models.BooleanField(default=False)


class GroupCourse(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Teaches(models.Model):
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    is_fall = models.BooleanField(default=False)


class Poll(models.Model):
    poll_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()
    # teachers = models.ForeignKey(Teaches, on_delete=models.CASCADE, default=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def open(self):
        now = timezone.now()
        return self.open_date <= now <= self.close_date

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Votes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)


# 0 is for 1 choice questions
# 1 is for many choice questions
# 2 is for input text
class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    type = models.SmallIntegerField(default='0')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    @classmethod
    def create_choice(cls, question_id, choice):
        return cls(question=question_id, choice_text=choice, votes=1)

    @classmethod
    def add_choice(cls, question, choice):
        try:
            c = question.choice_set.get(choice_text = choice)
            c.votes += 1
            return c
        except(cls.DoesNotExist, cls.MultipleObjectsReturned):
            return cls.create_choice(question, choice)


