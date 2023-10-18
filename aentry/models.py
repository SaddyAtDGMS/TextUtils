from django.db import models
from django.utils import timezone
import datetime

# Create your models here.



class mine_details(models.Model) :
    minecode = models.CharField(max_length=12)
    minename = models.CharField(max_length=100)
    ownercode = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class acc_detail(models.Model) :
    minecode = models.ForeignKey(mine_details, on_delete=models.CASCADE)
    minename = models.CharField(max_length=100)
    acc_date = models.DateTimeField("Accident Date")
    killed = models.IntegerField(default=0)
    injured = models.IntegerField(default=0)
    coscode = models.CharField(max_length=4)

    def __str__(self):
        return self.name


