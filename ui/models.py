from django.db import models

# THIS IS DATABASE STUFF


class Stage(models.Model):
    title = models.CharField(max_length=255)
    length = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class Question(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    q_num = models.IntegerField()
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.question_text

