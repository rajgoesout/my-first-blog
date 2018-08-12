"""
Here (in models.py) we define all objects called Models
"""
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """models.Model means that the Post is a Django model,
    so django knows that it should be saved in the database"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # this is a link to another model: when the referenced object is deleted, also delete the objects that have references to it
    title = models.CharField(max_length=200)  # define text with a limited number of characters
    text = models.TextField()  # for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)  # this is a date and time
    published_date = models.DateTimeField(blank=True, null=True) # blank=True means this field can be left blank, null=True means it can can null in the database

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
