from django.db import models

# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True) # change later
    progress = models.IntegerField()
    description = models.TextField()