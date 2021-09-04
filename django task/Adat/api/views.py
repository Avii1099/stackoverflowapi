from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from rest_framework import serializers, views
from rest_framework.response import Response
from api.models import ApiModel
from django.shortcuts import render

from .serializers import ApiSerializers
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets 
import requests
import json
# Create your views here.

class ApiList(viewsets.ModelViewSet):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializers

def getdata(request, value):
    global data
    if value:
        res = requests.get('http://localhost:8000/apiv/')
        data = res.json()
        return render(request, 'api/showdata.html', {'data': data, 'value':value})
    else:
        return render(request, 'api/showdata.html', {'data': data})

def clickbutton(request):
    return render(request, 'api/click.html')



