from rest_framework import viewsets,permssions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import *
from main.serializers import *

@api_view(['GET, 'POST'])
def part_list(request, format=None):
    if request.method == 'GET':
        snippets =

@api_view(['GET', 'PUT', 'DELETE'])
def part_detail(request, id, format=None):
    try:
        snippet = 