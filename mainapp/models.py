from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms import ClearableFileInput

STATUS = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('otheres', 'Others'),
)


class Profile(models.Model):
    gender = models.CharField(max_length=50, choices=GENDER, default=GENDER[0][0])
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0][0])
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.user.username






class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=30,blank=True)
    model_Name = models.CharField(max_length=30,blank=True)
    model_Variant = models.CharField(max_length=30,blank=True)
    engine = models.CharField(max_length=30,blank=True)
    year = models.CharField(max_length=30,blank=True)
    car_number = models.CharField(max_length=50,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='vehicles')

    def __str__(self):
        return  self.user.username


class Bank(models.Model):
    account_name = models.CharField(max_length=30,blank=True)
    account_number = models.CharField(max_length=30,blank=True)
    balance = models.FloatField(default=0)
    primary=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bank_accounts')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class VehiclePass(models.Model):
    car_number=models.CharField(max_length=30 ,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField('Upload ', upload_to='uploads/')

    def __str__(self):
        return self.file_upload.name

class VehiclePassForm(forms.ModelForm):
    class Meta:
        model = VehiclePass
        fields = ['file_upload']
        widgets = {
            'file_upload': ClearableFileInput(attrs={'multiple': True}),
        }


# delete the file_upload files associated with each object or record
@receiver(post_delete, sender=VehiclePass)
def submission_delete(sender, instance, **kwargs):
    instance.file_upload.delete(False)
