from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    period_date = models.DateTimeField('date published')
