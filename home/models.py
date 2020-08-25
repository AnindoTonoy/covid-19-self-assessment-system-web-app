from django.db import models

# Create your models here.
class Result(models.Model):
    age = models.CharField(max_length=122)
    sex = models.CharField(max_length=122)
    temperature = models.CharField(max_length=122)
    assessment_date = models.DateField()
    assessment_score = models.CharField(max_length=122)
    covid19_result = models.CharField(max_length=122)
