# django_blog/urls.py

from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include
from blog.views import home, profile_view, register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', home, name='home'),  # Add this line for the homepage
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),


    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('', include('blog.urls')),  # Include blog app URLs if you have specific ones there
]
