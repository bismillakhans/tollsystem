import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login
# Create your views here.
from mainapp.forms import SignUpForm, ProfileForm, UserForm,VehicleForm,BankForm
# from mainapp.models import VehiclePass, VehiclePassForm
from mainapp.models import VehiclePassForm, VehiclePass,Vehicle,Bank
from tollsettings import parser


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

        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            profile_form.save()

            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('index')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,

    })

def addVehicle(request):
    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():


            note= vehicle_form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, ('Your vehicle added successfully !'))
            return redirect('index')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        vehicle_form=VehicleForm()
    vehicle=Vehicle.objects.filter(user=request.user)
    return render(request,'accounts/vehicle_form.html',{
        'vehicle_form':vehicle_form,
        'vehicles' : vehicle
    })

def addBank(request):
    if request.method == 'POST':
         bank_form=BankForm(request.POST)
         if bank_form.is_valid():
             note= bank_form.save(commit=False)
             note.user = request.user
             note.save()
         else:
            messages.error(request, ('Please correct the error below.'))
    else:
        bank_form=BankForm()
    bank=Bank.objects.filter(user=request.user)
    return render(request,'accounts/bank_form.html',{
        'bank_form':bank_form,
        'banks' : bank
    })
def vehicle_passing(request):

    if request.method == 'POST':
            file_form = VehiclePassForm(request.POST, request.FILES)
            files = request.FILES.getlist('file_upload')

            if file_form.is_valid():
                for file in files:
                    try:
                        # saving the file
                        # user = request.user

                        # saving the file
                        file_upload = VehiclePass(file_upload=file)
                        file_upload.save()
                        output = parser.PlateParser(os.path.join(settings.MEDIA_ROOT, file_upload.file_upload.name))
                        data = output.get_extracted_data()

                        file_upload.car_number=data.get('name')
                        file_upload.save()
                    except IntegrityError:
                        messages.warning(request, 'Duplicate resume found:', file.name)
                        return redirect('homePage')
                documents = VehiclePass.objects.all()
                messages.success(request, ' Updated!')
                context = {
                    'documents': documents,
                }
                return render(request, 'homePage.html', context)
    else:
        form = VehiclePassForm()
    return render(request, 'homePage.html', {'form': form})


