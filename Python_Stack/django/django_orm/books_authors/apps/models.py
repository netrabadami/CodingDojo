from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    note = models.TextField()
    books = models.ManyToManyField(Books, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
