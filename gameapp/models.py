from django.db import models

# Create your models here.
class cls(models.Model):
    name1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20)
    result =models.CharField(max_length=50,default="")