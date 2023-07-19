from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password
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
    last_login = models.DateTimeField(null=True, blank=True)
   
    def __str__(self):
        return self.nickname

    def get_email_field_name(self):
        return 'email'

 ###################################################################################<<<<<<<<< Model for Creator registration form>>>>>>>>>>>>>>>>>


# Create Artist Profile
class Profile_artist(models.Model):
    user = models.ForeignKey(User_Registration, on_delete=models.SET_NULL, null=True, blank=True)
    firstname = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=255,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    marital_status = models.CharField(max_length=255,blank=True,null=True)
    profection = models.CharField(max_length=255,blank=True,null=True)
    height = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    interests = models.TextField(blank=True,null=True)
    hobbies = models.TextField(blank=True,null=True)
    passions = models.TextField(blank=True,null=True)
    goals = models.TextField(blank=True,null=True)
    achievements = models.TextField(blank=True,null=True)
    social_media_links = models.TextField(blank=True,null=True)
    skills = models.TextField(blank=True,null=True)
    awards = models.TextField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)

    
    def _str_(self):
        return f"{self.firstname} {self.lastname}"



 ###################################################################################<<<<<<<<< Model for Artist registration form >>>>>>>>>>>>>>>>>





###################################################################################<<<<<<<<< Confirm registration for creator >>>>>>>>>>>>>>>>>




###################################################################################<<<<<<<<< Confirm registration for Artist >>>>>>>>>>>>>>>>>


