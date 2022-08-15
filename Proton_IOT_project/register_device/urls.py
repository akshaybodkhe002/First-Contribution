from atexit import register
from django.contrib import admin
from django.urls import path, include
from register_device import views

urlpatterns = [
    path('',views.dashboard ),
    
    path('reg_form/', views.form, name="form"),
    # path('reg_form/', views.form, name="form"),
]
