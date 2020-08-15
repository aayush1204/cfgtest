from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("movies/", MovieView.as_view(), name="Appointment"),
    path("singlemovie/", MovieSingleView.as_view(), name="moviesingle"),
   
]