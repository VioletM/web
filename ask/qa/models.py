from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime as dt

class Question(models.Model):

    class QuestionManager(models.Manager):
        def new(self):
            return self.order_by('-added_at')

        def popular(self):
            return self.order_by('-rating')

    object = QuestionManager()
    title = models.CharField(max_length=250)
    text = models.TextField()
    added_at = models.DateField(default=dt.datetime.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='question_like_user')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=dt.datetime.now)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)



