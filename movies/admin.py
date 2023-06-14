from django.contrib import admin
from .models import (Movie, MovieShots, RatingStar, Rating, Reviews, Genre, Actor, Category)

admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Category)


