from django.contrib import admin
from .models import UserProfileInfo, User, blood_donator,clothes_donator,food_donator

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(blood_donator)
admin.site.register(clothes_donator)
admin.site.register(food_donator)
