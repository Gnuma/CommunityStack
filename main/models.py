from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    time_reading = models.IntegerField()
    link = models.URLField()
    author_name = models.CharField(max_length=255)
    author_img = models.URLField()
    last_updated = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
