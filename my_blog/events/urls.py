from django.urls import path, include

from . import views

urlpatterns = [
    path('events/', views.events_list),
    path('users/<slug>/', views.event_detail),
]
