from django.urls import path

from apps.bookmarker.views import categories
from .views import dashboard


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('categories/', categories, name='categories'),
]