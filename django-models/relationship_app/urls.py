# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
# relationship_app/urls.py
urlpatterns = [
    # URL pattern for user login with custom template
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # URL pattern for user logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # URL pattern for user registration
    path('register/', register, name='register'),
]