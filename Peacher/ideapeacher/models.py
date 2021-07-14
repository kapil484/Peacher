from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.



class MyUser(models.Model):
    user = models.OneToOneField(User, null= True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null= True)
    idprove = models.CharField(max_length=50, null=True)
    idproveno = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=10, null=True)

class category(models.Model):
    category = models.CharField(max_length=100)

class idea(models.Model):
    peacher = models.ForeignKey(MyUser, on_delete=models.CASCADE,default=False)
    Post_idea = models.TextField()
    date_created = models.DateTimeField(default = datetime.now())
    pdf = models.FileField(upload_to="book/pdfs",blank=True)
    category =models.ManyToManyField(category)

    def __str__(self):
        return self.Post_idea