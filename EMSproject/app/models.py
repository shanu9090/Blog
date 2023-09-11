from django.db import models


# Create your models here.
class AdminDB(models.Model):
    Fname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=10)
    def __str__(self):
        return self.Fname

class UserDB(models.Model):
    Fname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=10)
    def __str__(self):
      return self.Fname
    
class EnquiryDB(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Contact=models.IntegerField()
    Quiry=models.CharField(max_length=500)
    def __str__(self):
      return self.Fname
    