from django.db import models

# Create your models here.
class User(models.Model):
    Student_Name = models.CharField(max_length=70)
    Father_Name = models.CharField(max_length=70)
    Contact_Number = models.CharField(max_length=70)
    Address = models.CharField(max_length=70)
    Course = models.CharField(max_length=70)
    Timing = models.CharField(max_length=70)
    Days = models.CharField(max_length=70)