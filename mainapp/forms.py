from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mainapp.models import  Profile,Vehicle,Bank


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('gender','bio','location','birth_date')

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('manufacturer','model_Name','model_Variant','engine','year','car_number')

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('account_name','account_number')

class VehicleNumberForm(forms.Form):
    car_number= forms.CharField(label='Car Number', max_length=12)
