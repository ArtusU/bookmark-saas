from django.urls import path

from apps.bookmarker.views import (
    categories,
    category,
    category_add,
    bookmark_add,
    category_edit,
)
from .views import dashboard


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("categories/", categories, name="categories"),
    path("categories/<int:category_id>/", category, name="category"),
    path("categories/add/", category_add, name="category_add"),
    path("categories/<int:category_id>/edit/", category_edit, name="category_edit"),
    path(
        "categories/<int:category_id>/add_bookmark", bookmark_add, name="bookmark_add"
    ),
]
