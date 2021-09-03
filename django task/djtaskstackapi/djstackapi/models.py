from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=350)
    votecount = models.IntegerField(default=0)
    views = models.CharField(max_length=50)
    tags = models.CharField(max_length=350)

    def __str__(self):
        return self.question
