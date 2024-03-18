# views.py
from django.shortcuts import render
from movieapp.models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})
