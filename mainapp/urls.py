from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainapp import views
urlpatterns = [    
    
    path('index/',views.index,name='index'),
    path('',views.homePage,name='homePage'),
    path('vehicle_detail/',views.addVehicle,name='vehicle_detail'),
    path('bank_detail/',views.addBank,name='bank_detail'),
    path('edit_profile/',views.update_profile,name='edit_profile'),
    path('signup/',views.signup,name='signup')
]