from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.my_endpoint, name = 'my_endpoint'),
]