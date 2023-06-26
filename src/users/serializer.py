from rest_framework import serializers
from .models import *


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'