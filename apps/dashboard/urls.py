from django.urls import path

from apps.bookmarker.views import (
    categories,
    category,
    category_add,
    bookmark_add,
    category_edit,
    category_delete,
    bookmark_edit,
)
from .views import dashboard


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("categories/", categories, name="categories"),
    path("categories/<int:category_id>/", category, name="category"),
    path("categories/add/", category_add, name="category_add"),
    path("categories/<int:category_id>/edit/", category_edit, name="category_edit"),
    path(
        "categories/<int:category_id>/delete/", category_delete, name="category_delete"
    ),
    path(
        "categories/<int:category_id>/add_bookmark", bookmark_add, name="bookmark_add"
    ),
    path(
        "categories/<int:category_id>/edit_bookmark/<int:bookmark_id>/",
        bookmark_edit,
        name="bookmark_edit",
    ),
]
