from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)#model class to add additonal info which the original user class does not has

    #additonal classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
            return self.user.username

class blood_donator(models.Model):

     user_name = models.CharField(max_length=255)
     email = models.EmailField(max_length=255,unique=False)
     blood_type = models.CharField(max_length=255)
     medical_hist = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     medical_docs = models.ImageField(upload_to='medical_docs_pic',blank=True)

     def __str__(self):
             return self.user_name

class food_donator(models.Model):

     user_name = models.CharField(max_length=255)
     email = models.EmailField(max_length=255,unique=True)
     food_type = models.CharField(max_length=255)
     quantity = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     cooking_date = models.DateTimeField(default=timezone.now)

     def __str__(self):
             return self.user_name

class clothes_donator(models.Model):

     user_name = models.CharField(max_length=255)
     email = models.EmailField(max_length=255,unique=True)
     clothes_type = models.CharField(max_length=255)
     quantity = models.CharField(max_length=255)
     location = models.CharField(max_length=255)

     def __str__(self):
             return self.user_name
