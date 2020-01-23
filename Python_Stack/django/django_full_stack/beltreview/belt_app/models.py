from django.db import models
import re
import bcrypt
from django.contrib import messages
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# email validation - must follow standard email format
PW_REGEX = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')
# password validation - must be at least 8 char, have 1 number, 1 lowercase, 1 uppercase

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 2:
            errors["name"] = "First name must be at least 2 characters long."
        if len(postData["alias"]) < 2:
            errors["alias"] = "Alias must be at least 2 characters long."
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email address."
        if not PW_REGEX.match(postData["password"]):
            errors["password"] = "Passwords must be at least 8 characters long."
        if postData["password"] != postData["conf_password"]:
            errors["password_match"] = "Passwords do not match!"
        return errors

    def loginValidator(self, postData):
        user = User.objects.filter(email = postData["login_email"])
        errors = {}
        if not user:
            errors['email'] = "Please enter a valid email address."
        if user and not bcrypt.checkpw(postData["log_password"].encode('utf-8'), user[0].pw_hash.encode('utf-8')):
            errors['password'] = "Invalid password."
        return errors
class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    book_owner = models.ForeignKey(User,related_name='bookowner',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review=models.TextField()
    rating=models.IntegerField()
    book=models.ForeignKey(Books,related_name='book_review',on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User,related_name='book_reviews',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)