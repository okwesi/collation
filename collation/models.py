from django.db import models

from constituency.models import Constituency, Region

# Create your models here.

class Vote(models.Model):
    region = models.ForeignKey(Region,  on_delete=models.DO_NOTHING)
    constituency = models.ForeignKey(Constituency,  on_delete=models.DO_NOTHING)
    ndc_vote = models.IntegerField()
    npp_vote = models.IntegerField()
    other_vote = models.IntegerField()
    datetime = models.DateTimeField( auto_now=True, auto_now_add=False)

    
    