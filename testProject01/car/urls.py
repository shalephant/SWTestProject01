from django.urls import path
from . import views

urlpatterns = [
    path('', views.SelectCarView.as_view(), name="SelectCars"),
    path('delete/<int:pk>', views.DeleteCarView.as_view(), name="DeleteCar"),
    path('add', views.AddCarView.as_view(), name="AddCar")
]