from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    bookmarks = request.user.bookmarks.all().order_by("-created_at")[0:5]
    categories = request.user.categories.all().order_by("-created_at")[0:5]

    context = {"bookmarks": bookmarks, "categories": categories}
    return render(request, "dashboard/dashboard.html", context)


@login_required
def settings(request):
    return render(request, "dashboard/settings.html")
