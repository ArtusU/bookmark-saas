from django.urls import path

from apps.bookmarker.views import categories, category
from .views import dashboard


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('categories/', categories, name='categories'),
    path('categories/<int:category_id>', category, name='category'),
]