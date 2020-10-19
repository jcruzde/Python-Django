from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:recurso>', views.nuevo),
]