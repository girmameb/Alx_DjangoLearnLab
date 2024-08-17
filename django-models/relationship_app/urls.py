# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    # URL pattern for user login with a custom template
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # URL pattern for user logout, redirecting to login page after logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # URL pattern for user registration
    path('register/', register, name='register'),

    # URL pattern for listing books
    path('books/', list_books, name='list_books'),

    # URL pattern for library detail view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
