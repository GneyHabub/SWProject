from django.db import models

# Create your models here.
import datetime
from django.db import models
from django import forms
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=64) #full name
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    role = models.SmallIntegerField()
# 0 is for student
# 1 is for prof
# 2 is for higher authorities (doe members)
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=16) #i.e. BS18-06

    

class Poll(models.Model):
    poll_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()
    allowed_users = models.ManyToManyField(User)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def open(self):
        now = timezone.now()
        return self.open_date <= now <= self.close_date

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# 0 is for 1 choice questions
# 1 is for many choice questions
# 2 is for input text
class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    type = models.SmallIntegerField(default='0')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    @classmethod
    def create_choice(cls, question_id, choice):
        return cls(question=question_id, choice_text=choice, votes=1)


