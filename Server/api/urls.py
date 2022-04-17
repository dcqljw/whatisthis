from django.urls import path
from api import views

urlpatterns = [
    path('xby', views.one_url),
    path('create_article', views.create_article),
    path('create_short_link', views.short_link)
]
