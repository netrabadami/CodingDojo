from django.db import models
from datetime import datetime
# Create your models here.

class ShowManager(models.Manager):
    def basic_validation(self,postData):
        error = {}
        if len(postData["title"]) < 2:
            error["title"] = "Title must be at least 2 characters."
        if len(postData["network"]) < 3:
            error["network"] = "Network must be at least 3 characters."
        if len(postData["description"]) < 10 and len(postData["description"]) > 0:
            error["description"] = "Description must be at least 10 characters."
        if len(postData["release_date"]) > 0 and datetime.strptime(postData["release_date"], '%Y-%m-%d') > datetime.today() :
            error["release_date"] = "Invalid release date."
        return error
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


    
    
    
    
    
    
    