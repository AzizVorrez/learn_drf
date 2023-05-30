from rest_framework.serializers import ModelSerializer
from shop.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['date_created', 'date_updated', 'name', 'description', 'category']

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['date_created', 'date_updated', 'name', 'description', 'price']