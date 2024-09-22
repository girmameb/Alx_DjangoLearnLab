# blog/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm  # Ensure you create this form

# blog/views.py

from .forms import CustomUserCreationForm  # Ensure this line is correct


class PostListView(ListView):
    model = Post
    template_name = 'blog/templates/posts/post_list.html'  # Specify your templates
    context_object_name = 'posts'  # Default is 'object_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/templates/posts/post_detail.html'  # Specify your templates
    context_object_name = 'blog'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/templates/posts/post_form.html'  # Specify your templates
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/templates/post_form.html'  # Specify your templates
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author is set
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to edit


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'  # Specify your templates
    success_url = reverse_lazy('blog-list')  # Redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to delete


# blog/views.py

from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'blog/home.html')  # Create this templates


# blog/views.py

from django.shortcuts import render

# blog/views.py

from django.shortcuts import render


def register(request):
    return render(request, 'blog/register.html')  # Create this templates


# blog/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'  # Adjust the path as necessary


class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'  # Ensure this templates exists


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('list_posts')  # Redirect to the list of posts or post detail
        return redirect('list_posts')  # Handle errors appropriately

class CommentUpdateView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:  # Ensure the user is the comment author
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('list_posts')  # Redirect after updating
        return redirect('list_posts')  # Handle errors appropriately

class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:  # Ensure the user is the comment author
            comment.delete()
            return redirect('list_posts')  # Redirect after deletion
        return redirect('list_posts')  # Handle errors appropriately
from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()  # No results if no query

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
