from django import template
from movies.models import Category, Movie


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()



@register.inclusion_tag(r'C:\Users\day26\PycharmProjects\pythonProject2\Django\django_movie\templates\movies\tag\last_movies.html')
def get_last_movie(num=3):
    last_movies = Movie.objects.order_by("id")[:num]
    return {'last_movies': last_movies}