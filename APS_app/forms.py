from django import forms
from django.contrib.auth.models import User
from APS_app.models import UserProfileInfo, food_donator, blood_donator, clothes_donator

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class blood_donator_form(forms.ModelForm):
    class Meta():
        model = blood_donator
        fields = ('user_name','email','medical_hist','blood_type','medical_docs','location')

class food_donator_form(forms.ModelForm):
    class Meta():
        model = food_donator
        fields = ('user_name','email','cooking_date','food_type','quantity','location')

class clothes_donator_form(forms.ModelForm):
    class Meta():
        model = clothes_donator
        fields = ('user_name','email','clothes_type','quantity','location')
