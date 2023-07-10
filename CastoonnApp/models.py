from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class User_Registration(models.Model):
    
    name = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    nickname = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    phone_otp = models.IntegerField(null=True,blank=True)
    email = models.EmailField()
    email_otp =models.IntegerField(null=True,blank=True)
    profession = models.CharField(max_length=255,blank=True,null=True)
    experience = models.IntegerField(null=True)
    role = models.CharField(max_length=255,blank=True,null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname



 ###################################################################################<<<<<<<<< Model for Creator registration form>>>>>>>>>>>>>>>>>






 ###################################################################################<<<<<<<<< Model for Artist registration form >>>>>>>>>>>>>>>>>





###################################################################################<<<<<<<<< Confirm registration for creator >>>>>>>>>>>>>>>>>




###################################################################################<<<<<<<<< Confirm registration for Artist >>>>>>>>>>>>>>>>>


