from django.urls import path
from . import views

app_name = 'concerts'

urlpatterns = [
    path('concerts/', views.home, name='home'),
    path('concerts/<str:artist_id>/',
         views.show_concerts_and_news, name='show_concerts_and_news'),
    path('news/<str:keywords>/', views.show_news, name='show_news'),
]
