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
    tags = forms.CharField(
        max_length=200,
        required=False,
        help_text='Comma-separated list of tags.'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tags_input = self.cleaned_data.get('tags')
        if tags_input:
            # Split tags by commas and strip whitespace
            tags = [tag.strip() for tag in tags_input.split(',')]
            return tags
        return []

    def save(self, commit=True):
        post = super().save(commit)
        # Save the tags
        for tag in self.cleaned_data['tags']:
            post.tags.add(tag)  # This assumes tags are being added to the Post model directly
        if commit:
            post.save()
        return post