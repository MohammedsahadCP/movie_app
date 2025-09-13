from django.urls import path
from my_app import views

urlpatterns=[
    path('text/',views.any,name="anyyy")
]