from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SponerUser(models.Model):
    user = models.OneToOneField(User, null= True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null= True)
    idprove = models.CharField(max_length=50, null=True)
    idproveno = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=10, null=True)