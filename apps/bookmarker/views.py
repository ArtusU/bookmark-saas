from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def categories(request):
    categories = request.user.categories.all()
    context = {
        categories: categories
    }
    return render(request, 'bookmarker/categories.html', context)