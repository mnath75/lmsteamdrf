from django.shortcuts import render


# Create your views here.
from django.shortcuts import render
from .serializers import HomeSerializer
from rest_framework import viewsets
from .models import Home
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import status,permissions
from knox.auth import TokenAuthentication

class HomeModelViewSet(viewsets.ModelViewSet):
  queryset = Home.objects.all()
  serializer_class = HomeSerializer
