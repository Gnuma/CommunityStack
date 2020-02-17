from django.contrib import admin
from .models import Category, Topic, User, Tutorial

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Tutorial)
admin.site.register(User)
