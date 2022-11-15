from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Category


@csrf_exempt
def api_delete_category(request, category_id):
    category = request.user.categories.all().get(pk=category_id)
    category.delete()

    return JsonResponse({"success": True})
