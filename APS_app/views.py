from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm, blood_donator_form,clothes_donator_form,food_donator_form

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'APS_app/index.html')

def upcoming(request):
    return render(request,'APS_app/upcoming.html')

def services(request):
    return render(request,'APS_app/services.html')

def about(request):
    return render(request,'APS_app/about.html')

def contact(request):
    return render(request,'APS_app/contact.html')

def food(request):
    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = food_donator_form(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() :

            # Save User Form to Database
            user = user_form.save(commit=False)

            user.save()

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = food_donator_form()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'APS_app/food.html',
                          {'user_form':user_form,})

def blood(request):
    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = blood_donator_form(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() :

            # Save User Form to Database
            user = user_form.save(commit=False)

            user.save()

            if 'medical_docs_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.medical_docs = request.FILES['medical_docs_pic']

            # Now save model
            user.save()

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = blood_donator_form()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'APS_app/blood.html',
                          {'user_form':user_form,})


def clothes(request):
    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = clothes_donator_form(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() :

            # Save User Form to Database
            user = user_form.save(commit=False)

            user.save()

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = clothes_donator_form()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'APS_app/clothes.html',
                          {'user_form':user_form,})

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/app4/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False #tell if Someone is registered or not

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'registration/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'registration/login.html', {})
