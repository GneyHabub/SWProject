from django.db import models

# Create your models here.
import datetime
from django.db import models
from django import forms
from django.utils import timezone


class Poll(models.Model):
    poll_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# 0 is for 1 choice questions
# 1 is for many choice questions
# 2 is for input text
class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    type = models.IntegerField(default='0')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    @classmethod
    def create_choice(cls, question_id, choice):
        return cls(question=question_id, choice_text=choice, votes=1)

