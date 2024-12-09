from django.urls import path
from . import views

urlpatterns = [
    path('create_brand', views.create_brand, name='create_brand'),
]