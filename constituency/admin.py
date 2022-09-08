from django.contrib import admin

from constituency.models import Constituency, Region

# Register your models here.
admin.site.register(Region)
admin.site.register(Constituency)