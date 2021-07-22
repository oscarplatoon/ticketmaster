from django.urls import path
from . import views



urlpatterns = [
    # path('', views.events_list, name='events_list'),
    path('search_events/', views.search_events, name="search_events"),
]