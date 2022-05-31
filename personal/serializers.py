from . models import Home
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['home_id','home_title','home_slug','home_logo']