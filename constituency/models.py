from django.db import models

# Create your models here.
class Region(models.Model):
    regional_code = models.CharField(max_length=10, unique=True, primary_key=True)
    regional_name = models.CharField(max_length=255)




class Constituency(models.Model):
    regional_code = models.ForeignKey(Region, on_delete=models.CASCADE)
    constituency_code = models.CharField(max_length=20, unique=True, primary_key=True)
    constituency_name = models.CharField(max_length=500)
    counted = models.BooleanField(default=False)