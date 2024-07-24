from django.urls import path
from . import views

urlpatterns = [
    path('shoes/', views.index, name='shoes'),
]