from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .forms import MovieForm

from movieapp.forms import MovieForm
from movieapp.models import Movie, Category


# Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     context = {'movie_list': movies}
#     return render(request, 'movie.html', context)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Category, Movie


def dummy(request):
    return render(request, 'dummy.html')

def movie_by_cat(request, c_slug=None):
    category = None
    movies = None
    if c_slug != None:

        category = get_object_or_404(Category, slug=c_slug)
        # movies_list = Movie.objects.filter(category=movie, available=True)
        movies = Movie.objects.filter(category=category)

    else:
        movies = Movie.objects.filter(category=category)

        # movies = Movie.objects.all()

    return render(request, "moviecat.html", {'category': category, 'movies': movies})

def movie_detail(request, category_slug, movie_slug):
    try:
        movie =Movie.objects.get( category__slug=category_slug, slug=movie_slug)
    # category = Category.objects.all()  # Fetch all categories
    except Exception as e:
        raise e
    return render(request, 'movie_detail.html', {'movie': movie})





def user_movie(request):
    movie = Movie.objects.all()

    context = {'movie_list': movie
               }
    return render(request, "user.html", context, )


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def movie_show(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie_show.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movieapp:movie')
        else:
            # Form data is invalid, print form errors
            print(form.errors)
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})




def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})


def delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')
        # return redirect('movieapp:movie_list')
    return render(request, 'delete.html', {'movie': movie})


# def movies_by_category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     movies = Movie.objects.filter(category=category)
#     return render(request, 'movies_by_category.html', {'category': category, 'movies': movies, })
#     # # c_page = None
    # # movie_list = None
    # # if category_slug != None:
    # #     c_page = get_object_or_404(Category, slug=category_slug)
    # #     movies = Movie.objects.all().filter(category=c_page, available=True)
    # # else:
    # #     products_list = Movie.objects.all().filter(available=True)
    # return render(request, 'movies_by_category.html', {'category': c_page, 'movies': movies, })