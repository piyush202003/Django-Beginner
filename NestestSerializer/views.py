from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def index(request):
    items_obj = Item.objects.all()
    serializer = ItemSerializer(items_obj, many=True)
    return Response({'status':200,'payload':serializer.data})
