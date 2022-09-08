import imp
from django.urls import path,re_path
from collation.views import *

urlpatterns = [
    re_path(r'^$', collation, name="collation"),
    path('create_collation/', create_collation, name="create_collation"),
    path('votes/', get_collation, name="get_collation"),
]

