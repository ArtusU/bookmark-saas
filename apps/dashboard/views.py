from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def dashboard(request):
    bookmarks = request.user.bookmarks.all().order_by("-created_at")[0:5]
    categories = request.user.categories.all().order_by("-created_at")[0:5]

    context = {"bookmarks": bookmarks, "categories": categories}
    return render(request, "dashboard/dashboard.html", context)


@login_required
def settings(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")

        user = request.user

        if username != request.user.username:
            users = User.objects.filter(username=username)

            if len(users):
                messages.error(request, "The username already exists!")
            else:
                user.username = username

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, "The changes was saved!")

        return redirect("dashboard")

    return render(request, "dashboard/settings.html")
