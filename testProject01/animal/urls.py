from django.urls import path
from . import views

urlpatterns = [
    path('', views.SelectAnimalView.as_view(), name="SelectAnimal"),
    path('delete/<int:pk>', views.DeleteAnimalView.as_view(), name="DeleteAnimal"),
    path('add', views.AddAnimalView.as_view(), name="AddAnimal")
]