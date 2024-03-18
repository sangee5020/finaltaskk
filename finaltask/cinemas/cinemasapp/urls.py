# urls.py
from django.urls import path
from . import views

app_name = 'cinemasapp'

urlpatterns = [
    path('', views.index, name='index.html'),
]
