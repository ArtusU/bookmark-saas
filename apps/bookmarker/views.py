from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Category
from .forms import CategoryForm

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


@login_required
def category_add(request):
    if request.method == 'POST':
        form =  CategoryForm(request.POST)
        
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            
            return redirect('categories')
        
    else:
        form = CategoryForm()
        
    context = {
        'form' : form,
    }
    return render(request, 'bookmarker/category_add.html', context)