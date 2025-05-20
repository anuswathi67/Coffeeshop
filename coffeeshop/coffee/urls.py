from django.urls import path
from . import views

app_name = 'coffee' 

urlpatterns = [
    path("", views.home)
]
