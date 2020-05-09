from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image'
        ]
