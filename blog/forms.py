from django import forms
from blog.models import Blog

class FormsBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "image", "is_active"]

