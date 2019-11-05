from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login
# Create your views here.
from mainapp.forms import SignUpForm, ProfileForm, UserForm
from mainapp.models import VehiclePass, VehiclePassForm


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


def base(request):
    return render(request,'base.html')

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

# @login_required
# def edit_profile(request):
#     user = request.user
#     form = ProfileForm(request.POST or None, initial={'gender': user.profile.gender,
#                                                       'bio': user.profile.bio,'location': user.profile.location,'birth_date': user.profile.birth_date,    })
#     if request.method == 'POST':
#         if form.is_valid():
#             user.profile.gender = request.POST['gender']
#             user.profile.bio = request.POST['bio']
#             user.profile.location = request.POST['location']
#             user.profile.date_birth = request.POST['date_birth']
#
#             user.save()
#             return redirect('profile')
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "accounts/profile_edit.html", context)



@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
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
        'profile_form': profile_form
    })


def vehicle_passing(request)

    if request.method == 'POST':
            file_form = VehiclePassForm(request.POST, request.FILES)
            files = request.FILES.getlist('image')
            vehicle_data = []
            if file_form.is_valid():
                for file in files:
                    try:
                        # saving the file
                        # user = request.user

                        # saving the file
                        image = VehiclePass( image=file)
                        image.save()


