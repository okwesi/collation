from django.shortcuts import render
from .models import Constituency, Region
from django.http import JsonResponse

# Create your views here.


def get_regions(request):
    regions = list(Region.objects.values())
    return JsonResponse({"data":regions})

def get_constituencies(request, regional_code):
    constituencies = list(Constituency.objects.filter(regional_code=regional_code).values())
    return JsonResponse({"data":constituencies})