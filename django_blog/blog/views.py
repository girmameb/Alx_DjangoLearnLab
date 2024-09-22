# blog/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

from django.shortcuts import render


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
