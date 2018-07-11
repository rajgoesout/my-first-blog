from django.contrib import admin
from .models import Post  # import the model Post from models.py

admin.site.register(Post)  # to make our model visible on the admin page, register the model
