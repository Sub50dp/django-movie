from django.urls import path
from . import views
# 1
urlpatterns = [
    path("", views.MoviesView.as_view(), name="main"),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail")
]