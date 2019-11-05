from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login
# Create your views here.
from mainapp.forms import SignUpForm, ProfileForm, UserForm,VehicleForm,BankForm
# from mainapp.models import VehiclePass, VehiclePassForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def index(request):
    return render(request,'index.html')


def homePage(request):
    return render(request,'homePage.html')


    


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        vehicle_form = VehicleForm(request.POST, instance=request.user)
        bank_form = BankForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid() and vehicle_form.is_valid() and bank_form.is_valid():
            user_form.save()
            profile_form.save()
            vehicle_form.user=request.user
            vehicle_form.save()
            bank_form.user=request.user
            bank_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('index')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        vehicle_form = VehicleForm(instance=request.user)
        bank_form = BankForm(instance=request.user)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'vehicle_form':vehicle_form,
        'bank_form' : bank_form
    })


# def vehicle_passing(request)

#     if request.method == 'POST':
#             file_form = VehiclePassForm(request.POST, request.FILES)
#             files = request.FILES.getlist('image')
#             vehicle_data = []
#             if file_form.is_valid():
#                 for file in files:
#                     try:
#                         # saving the file
#                         # user = request.user

#                         # saving the file
#                         image = VehiclePass( image=file)
#                         image.save()


