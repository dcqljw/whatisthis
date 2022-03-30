from django.urls import path
from api import views

urlpatterns = [
    path('index', views.index),
    path('xby', views.one_url),
    path('create_one', views.create_article),
    path('create_short_link', views.short_link)
]
