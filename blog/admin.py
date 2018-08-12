from django.contrib import admin
from .models import Post, Comment  # import the models Post and Comment from models.py

admin.site.register(Post)  # to make our model visible on the admin page, register the model
admin.site.register(Comment)
