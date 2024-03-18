from django.contrib import admin

from .models import Category, Movie


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'year', 'youtube_link', 'comments', 'ratings', 'img']
    list_editable = ['youtube_link', 'comments', 'ratings']
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Movie, MovieAdmin)
