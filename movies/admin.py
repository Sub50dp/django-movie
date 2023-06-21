from ckeditor_uploader import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import (Movie, MovieShots, RatingStar, Rating, Reviews, Genre, Actor, Category)
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Category)
class CategoruAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "id",)


class ReviewsInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")

class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ["get_image"]
    def get_image(self, obj):
        return mark_safe(f"<image src={obj.image.url} width='70' height=auto")

    get_image.short_description = "Фото"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "url", "draft",)
    list_display_links = ("title",)
    list_filter = ("category", "year")
    search_fields = ("title", "category__name__startswith")
    inlines = [MovieShotsInLine, ReviewsInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ["get_image"]
    form = MovieAdminForm
    fieldsets = [
        (None, {"fields": (("title", "tagline", "draft",),)}),
        (None, {"fields": ("description", ("poster", "get_image"),)}),
        (None, {"fields": (("year", "country", "world_premiere"),)}),
        (None, {"fields": (("directors", "actors",),)}),
        (None, {"fields": (("category", "genres",),)}),
        (None, {"fields": (("budget", "fees_in_usa", "fees_in_world",),)}),
        (None, {"fields": (("url", "video_url",),)}),

    ]

    def get_image(self, obj):
        return mark_safe(f"<image src={obj.poster.url} width='70' height=auto")

    get_image.short_description = "Постер"
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fieldsets = [
        ("Название", {"fields": ("name",)}),
        (None, {"fields": (("description", "url"),)})
    ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ["get_image"]
    fieldsets = [
        (None, {"fields": (("name", "age", "get_image"),)}),
        (None, {"fields": ("description",)})
    ]

    def get_image(self, obj):
        return mark_safe(f"<image src={obj.image.url} width='50' height=auto")

    get_image.short_description = "Фото"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip",)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ["get_image"]

    def get_image(self, obj):
        return mark_safe(f"<image src={obj.image.url} width='50' height=auto")

    get_image.short_description = "Фото"

admin.site.register(RatingStar)
