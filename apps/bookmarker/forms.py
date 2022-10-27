from django.forms import ModelForm

from .models import Category, Bookmark

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        

class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title', 'description', 'url']
    