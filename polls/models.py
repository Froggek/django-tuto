from django.db import models


class Question(models.Model):
    # Field instance's name = field's name in DB (machine-readable name)
    question_text = models.CharField(max_length=200)
    # Human-readable name
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

