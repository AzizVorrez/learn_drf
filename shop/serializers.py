from rest_framework.serializers import ModelSerializer
from shop.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']