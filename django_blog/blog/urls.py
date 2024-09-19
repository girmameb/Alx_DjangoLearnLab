from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, profile_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),  # This should point to the profile_view in views.py
]
