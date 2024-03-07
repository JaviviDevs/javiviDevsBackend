from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
def get_csrf_token(request):
    # Obtener el token CSRF
    csrf_token = get_token(request)
    # Devolver el token CSRF en formato JSON
    return JsonResponse({'csrfToken': csrf_token})
