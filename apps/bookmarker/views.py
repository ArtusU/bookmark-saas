from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Category

@login_required
def categories(request):
    categories = request.user.categories.all()
    context = {
        'categories': categories
    }
    return render(request, 'bookmarker/categories.html', context)

 
@login_required
def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category
    }
    return render(request, 'bookmarker/category.html', context)