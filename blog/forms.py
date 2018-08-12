from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post # which model should be used to create this form
        fields = ('title', 'text') # which fields should be exposed in our form


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
