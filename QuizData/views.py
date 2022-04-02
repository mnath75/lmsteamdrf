from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from course.models import Topic
from .models import Language, Question,Ques
#from base.serializers import ProductSerializer, OrderSerializer

from rest_framework import status
from datetime import datetime
from .serializers import QuestionSerializer,QuesSerializer
from rest_framework import viewsets


class questionModelViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer


class quesModelViewSet(viewsets.ModelViewSet):
  queryset = Ques.objects.all()
  serializer_class = QuesSerializer# Create your views here.
