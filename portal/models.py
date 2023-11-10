from django.db import models

# Create your models here.

class AddJob(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField(max_length=600)
    job_type = models.CharField(max_length=15)
    job_location = models.CharField(max_length=50)

class Signup(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)