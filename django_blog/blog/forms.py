from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_blog.blog.models import Comment, Post, Tag


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only allow content to be set
from django import forms
from .models import Post
from taggit.models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags field
        widgets = {
            'tags': forms.CheckboxSelectMultiple()  # You can customize this widget
        }

    def clean_tags(self):
        # Optional: Clean and validate tags if needed
        tags = self.cleaned_data.get('tags')
        if not tags:
            raise forms.ValidationError("At least one tag is required.")
        return tags
