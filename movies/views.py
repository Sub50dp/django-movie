from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie
from .forms import ReviewForm
from .admin import ActorAdmin
from .admin import Actor
from .admin import GenreAdmin
class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    #  template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    # template_name = "movies/movie_detail.html" Django автоматически создает movie_detail

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            movie = Movie.objects.get(id=pk)
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolut_url())