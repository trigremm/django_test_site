# django_app/core/views.py
from django.http import JsonResponse


def ping_view(request):
    return JsonResponse({"status": "ok"})
