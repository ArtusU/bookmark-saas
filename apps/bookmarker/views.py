from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Category, Bookmark
from .forms import CategoryForm, BookmarkForm


@login_required
def categories(request):
    categories = request.user.categories.all()
    context = {"categories": categories}
    return render(request, "bookmarker/categories.html", context)


@login_required
def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {"category": category}
    return render(request, "bookmarker/category.html", context)


@login_required
def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()

            return redirect("categories")

    else:
        form = CategoryForm()

    context = {
        "form": form,
    }
    return render(request, "bookmarker/category_add.html", context)


@login_required
def category_edit(request, category_id):
    category = Category.objects.filter(created_by=request.user).get(pk=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)

    context = {"form": form, "category": category}

    return render(request, "bookmarker/category_edit.html", context)


@login_required
def bookmark_add(request, category_id):
    if request.method == "POST":
        form = BookmarkForm(request.POST)

        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.created_by = request.user
            bookmark.category_id = category_id
            bookmark.save()

            return redirect("category", category_id=category_id)
    else:
        form = BookmarkForm()

    context = {
        "form": form,
    }

    return render(request, "bookmarker/bookmark_add.html", context)
