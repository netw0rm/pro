from rest_framework import serializers

from main.models import *

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
