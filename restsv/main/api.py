from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class PartsList(APIView):
    def get(self, request, format=None):
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)
