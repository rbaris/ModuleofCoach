from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Module(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    dataSheet= models.FileField(null=True,blank=True)
    
    #cross validation holdout(veya kFold) miktari
    CVrate = models.FloatField(null=True,blank=True)
    kNeighbors = models.PositiveIntegerField(null=True,blank=True)
    metric =models.CharField(max_length=50,null=True,blank=True)
    isKNN = models.BooleanField(default= False)
    isDT = models. BooleanField(default=False)
    isNB = models.BooleanField(default=False)
    accuracy = models.FloatField(null=True,blank=True)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['accuracy']
