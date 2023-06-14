from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie

#1
class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    #  template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    # template_name = "movies/movie_detail.html" Django автоматически создает movie_detail