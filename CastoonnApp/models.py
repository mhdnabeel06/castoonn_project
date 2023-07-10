from django.db import models
from django.contrib.auth.models import User


# Create your models here.




 ###################################################################################<<<<<<<<< Model for Creator registration form>>>>>>>>>>>>>>>>>

class CreatorUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=50)
    experience = models.IntegerField(null=True)
    #adding user
    username = models.CharField(max_length=150,null=True)
    password = models.CharField(max_length=128,null=True)
    confirm_password = models.CharField(max_length=128,null=True)


    def __str__(self):
        return self.nickname
    




 ###################################################################################<<<<<<<<< Model for Artist registration form >>>>>>>>>>>>>>>>>


class ArtistUserProfile(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    phone_otp = models.IntegerField(null=True,blank=True)
    email = models.EmailField()
    email_otp =models.IntegerField(null=True,blank=True)
    profession = models.CharField(max_length=50)
    experience = models.IntegerField(null=True)

    def __str__(self):
        return self.nickname
    


###################################################################################<<<<<<<<< Confirm registration for creator >>>>>>>>>>>>>>>>>

# class CreatorUser(AbstractUser):
 
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)
#     confirm_password = models.CharField(max_length=128)



    # def save(self, *args, **kwargs):
        
    #     super().save(*args, **kwargs)


###################################################################################<<<<<<<<< Confirm registration for Artist >>>>>>>>>>>>>>>>>

# class ArtistUser(AbstractUser):
 
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)
#     confirm_password = models.CharField(max_length=128)



    # def save(self, *args, **kwargs):
        
    #     super().save(*args, **kwargs)
