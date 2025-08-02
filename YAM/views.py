from django.shortcuts import render

from django.http import JsonResponse
from .models import Site

def site_names(request):
    names = list(Site.objects.values_list('name', flat=True))
    return JsonResponse({'sites': names})
