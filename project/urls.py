from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset, AdminArticleViewset

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename="category")
router.register('product', ProductViewset, basename='products')
router.register('article', ArticleViewset, basename ='article')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('admin/articles', AdminArticleViewset, basename='admin-articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name = "token-obtain-pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token-refresh'),
    path('api/', include(router.urls)),
]
