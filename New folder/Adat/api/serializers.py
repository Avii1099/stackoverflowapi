from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import ApiModel


class ApiSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ApiModel
        fields = ('__all__')