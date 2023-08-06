from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    pan_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

