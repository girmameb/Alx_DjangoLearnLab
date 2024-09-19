from django.contrib import admin
from django.urls import path, include
from blog.views import profile_view, register, CustomLoginView, CustomLogoutView  # Ensure all views are imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include blog app URLs
    path('profile/', profile_view, name='profile'),  # Profile view
]
