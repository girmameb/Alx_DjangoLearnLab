from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post  # Ensure you're importing your Post model
from taggit.models import Tag

# Custom user creation form
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

# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only allow content to be set

# Post form with tagging functionality
from taggit.forms import TagWidget  # Adjust this import based on your TagWidget location

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=200,
        required=False,
        widget=TagWidget(),  # Use the TagWidget here
        help_text='Comma-separated list of tags.'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tags_input = self.cleaned_data.get('tags')
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(',')]
            return tags
        return []

    def save(self, commit=True):
        post = super().save(commit)
        if 'tags' in self.cleaned_data and self.cleaned_data['tags']:
            for tag in self.cleaned_data['tags']:
                post.tags.add(tag)  # Assuming Post model uses TaggableManager
        if commit:
            post.save()
        return post

