from django.db import models
from datetime import datetime

# Create your models here.
class Oziq_ovqat(models.Model):
    name = models.CharField(max_length=130,default = 'osh')
    type = models.CharField(max_length=50,default = ' ')
    surogi = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name
    
class Dokonlar(models.Model):
    name = models.CharField(max_length=150,default = ' ')
    location = models.CharField(max_length=200,default= ' ')

    def __str__(self) -> str:
        return self.name

    
