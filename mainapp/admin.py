from django.contrib import admin
from mainapp.models import Profile,Vehicle,Bank
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass