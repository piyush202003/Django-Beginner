from rest_framework import serializers
from .models import *

class GFGSerializer(serializers.ModelSerializer):
    class Meta:
        model = GFG
        fields = ['name',]

class ItemSerializer(serializers.ModelSerializer):
    name = GFGSerializer()

    class Meta:
        model = Item
        fields = '__all__'
        # depth = 1
    