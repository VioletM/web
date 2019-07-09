from __future__ import unicode_literals

import datetime as dt

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=250)
    text = models.TextField()
    added_at = models.DateField(default=dt.datetime.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def get_url(self):
        return reverse('qa:question-page', kwargs={'num': self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=dt.datetime.now)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
