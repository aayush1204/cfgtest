from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.serializers import UserSerializer, GroupSerializer ,MovieSerializer
from .models import Movie

from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
import datetime
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class MovieSingleView(APIView):
    def get(self, request):
          
        movie_id= request.query_params.get('id')
    
        temp1 = Movie.objects.filter(id=movie_id)

        ser = MovieSerializer(temp1, many=True)
        return Response(ser)

class MovieView(APIView):
    def get(self, request):
       
        temp = Movie.objects.all()
        ser = MovieSerializer(temp, many=True)
        return Response(ser.data)

    def post(self, request):
        title = request.POST['title']
        desc = request.POST['desc']
        year = request.POST['year']

        Movie.objects.create(title=title, desc = desc, year = year)

        ser = MovieSerializer(Movie.objects.all() , many =True)

        return Response(ser.data)

# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
   
#     def post(self, request, format=None):
#         # content = {
#         #     'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#         #     'auth': unicode(request.auth),  # None
#         # }
#         username = request.POST['username']
#         password = request.POST['password']
#         dict1 = {'id': "no aayush"}
#         if username == "aayush":
#             dict1={'id':"hello aayush"}
#         return Response(dict1)

   
