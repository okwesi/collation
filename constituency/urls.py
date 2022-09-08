from django.urls import path
from .views import *
urlpatterns = [
    path('regions/', get_regions, name="get_regions"),
    path('constituencies/<str:regional_code>', get_constituencies, name="get_constituencies")
]
