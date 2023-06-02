from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from shop.models import *

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['date_created', 'date_updated', 'name', 'description', 'price', 'product']

    def validate_price(self, value):
        if value < 1:
            raise ValidationError('Le prix doit être suppérieure à 1 €')
        return value
    
    def valide(self, value):
        if value.active is False :
            raise ValidationError('Le produit n\'est pas actif')
        return value



class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'date_updated', 'date_created']

class ProductDetailSerializer(ModelSerializer):

    articles = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['date_created', 'date_updated', 'name', 'description', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data
    

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name = value).exists():
            raise ValidationError('Ce nom existe déjà !')
        return value
    
    def validate(self, data):
        if data['name']  not in data['description']:
            raise ValidationError('Le nom doit être dans la description')
        
        return data

class CategoryDetailSerializer(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductDetailSerializer(queryset, many = True)
        return serializer.data