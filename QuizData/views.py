from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from course.models import Topic
from .models import Language, Question,Ques,Testmake,TestLayout,TestSection,TestSetting,TestQuestion,TestInstruction

#from base.serializers import ProductSerializer, OrderSerializer

from rest_framework import status
from datetime import datetime
from .serializers import QuestionSerializer,QuesSerializer,DlevelSerializer,LanguageSerializer,TestmakeSerializer,TestLayoutSerializer,TestSectionSerializer,LstmakeSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import TestInstructionSerializer,TestQuestionSerializer,TestSettingSerializer

class questionModelViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class quesModelViewSet(viewsets.ModelViewSet):
  queryset = Ques.objects.all()
  serializer_class = QuesSerializer

class testMakeModelViewSet(viewsets.ModelViewSet):
  queryset = Testmake.objects.all()
  serializer_class = TestmakeSerializer  

class testLayoutModelViewSet(viewsets.ModelViewSet):
  queryset = TestLayout.objects.all()
  serializer_class = TestLayoutSerializer    


class TestSectionModelViewSet(viewsets.ModelViewSet):
    queryset=TestSection.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['testmake']
    serializer_class = TestSectionSerializer

# class Lastmake(APIView):
#     def get(set,request format=None):
#         lastid=Testmake.objects.all().last().te_id
#         serializer=TestmakeSerializer

def lastmake(request):

    
    lastid=Testmake.objects.latest('te_id').te_id
    my_data = {
    "lastid": lastid,
    
}


    serializer=LstmakeSerializer(my_data)
    print("bbbbb",serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print("hahaha",json_data)
    return HttpResponse(json_data,content_type='application/json')
def filterdata(request):
    queryset=Ques.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['topic']
    print("asd",queryset)


class TestSettingModelViewSet(viewsets.ModelViewSet):
    queryset=TestSetting.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['testID']
    serializer_class = TestSettingSerializer
class TestQuestionModelViewSet(viewsets.ModelViewSet):
    queryset=TestQuestion.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['testID']
    serializer_class = TestQuestionSerializer 
class TestInstructionModelViewSet(viewsets.ModelViewSet):
    queryset=TestInstruction.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['testID']
    serializer_class = TestQuestionSerializer 