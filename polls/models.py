import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # Field instance's name = field's name in DB (machine-readable name)
    question_text = models.CharField(max_length=200)
    # Human-readable name
    pub_date = models.DateTimeField('date published')

    # __str__ isn important for:
    # the interactive prompt
    # the admin part
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
