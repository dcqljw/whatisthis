from django.urls import path
from api import views

urlpatterns = [
    path('index/', views.index),
    path('xby/', views.one_url),
    path('create/', views.create_article)
]
