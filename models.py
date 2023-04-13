from django.db import models

class Log(models.Model):
    points=models.CharField(max_length=200)
    date=models.DateField('date added')

    def __str__(self):
        return f"Date: {self.date},points:{self.points}pts"
# Create your models here.
