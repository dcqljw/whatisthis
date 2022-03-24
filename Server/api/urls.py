from django.urls import path
from api import views

urlpatterns = [
    path('index/', views.index),
]
