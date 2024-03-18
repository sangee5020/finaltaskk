from django.urls import path
from . import views

app_name='movieapp'

urlpatterns = [
    # path('movies/', views.movie_list, name='movie_list'),
    path('movie/', views.movie_by_cat, name='all_movies'),
    path('details/', views.user_movie, name='movie'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/',views.add_movie,name="add_movie"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/' ,views.delete,name='delete'),
    path('movie_show/<int:movie_id>/', views.movie_show, name='movie_show'),
    path('movie/details/<str:category_slug>/<str:movie_slug>/', views.movie_detail, name='movie_detail'),
    path('movie/<slug:c_slug>/', views.movie_by_cat, name='movie_by_cat'),
    path('movies/dummy',views.dummy,name='dummy'),

]
