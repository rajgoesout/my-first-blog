from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post # which model should be used to create this form
        fields = ('title', 'text',) # which fields should be exposed in our form
