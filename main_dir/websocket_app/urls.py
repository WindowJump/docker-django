from django.urls import path
from . import views

urlpatterns = [
    path('websocket_test/', views.index, name='main-page'),
]
