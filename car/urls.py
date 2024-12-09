from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarCreateView.as_view(), name='create_car'),
    path('details/<int:pk>/', views.DetailCarView.as_view(), name='car_details'),
    path('edit/<int:id>/', views.EditCarView.as_view(), name='edit_car'),
    path('delete/<int:id>/', views.DeleteCarView.as_view(), name='delete_car'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
]