from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movieapp:movie_by_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)





class Movie(models.Model):
    name=models.CharField(max_length=500)
    slug = models.SlugField(max_length=250, unique=True)
    desc=models.TextField(blank=True)
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery',blank=True)
    youtube_link = models.URLField(blank=True, null=True)
    comments = models.TextField(blank=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
    def get_url(self):
        return reverse('movieapp:movie_detail', args=[self.category.slug,self.slug])
    def __str__(self):
        return self.name
