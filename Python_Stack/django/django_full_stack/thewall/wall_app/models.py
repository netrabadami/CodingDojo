from django.db import models
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# email validation - must follow standard email format
PW_REGEX = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')
# password validation - must be at least 8 char, have 1 number, 1 lowercase, 1 uppercase

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["fname"]) < 2:
            errors["fname"] = "First name must be at least 2 characters long."
        if len(postData["lname"]) < 2:
            errors["lname"] = "Last name must be at least 2 characters long."
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
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Messages(models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    message = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

