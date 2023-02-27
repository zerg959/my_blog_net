from django.urls import path, include

from . import views

urlpatterns = [
    path('dogs/', views.dogs_list),
    path('dogs/<slug>/', views.dog_detail),
]
