from django.urls import path, include

from shop import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view())
]