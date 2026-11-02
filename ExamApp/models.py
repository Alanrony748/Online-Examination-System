from django.db import models

# Create your models here.

class QuestionDb(models.Model):
    question=models.CharField(max_length=500)
    option_a=models.CharField(max_length=500)
    option_b=models.CharField(max_length=500)
    option_c=models.CharField(max_length=500)
    option_d=models.CharField(max_length=500)
    correct_answer=models.CharField(max_length=500)


class AnswerDb(models.Model):
    answer=models.TextField()
    question_id=models.IntegerField()
    owner=models.CharField(max_length=200)
    points=models.PositiveIntegerField(null=True)
    submission_date=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(null=True)
