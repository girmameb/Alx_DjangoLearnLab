# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, list_books, LibraryDetailView
from .views import register, login, logout

urlpatterns = [
   
    # Login view with a custom template
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout view with redirect to login page
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # Registration view
path('registration/', register, name='register'),

    # Books list view
    path('books/', list_books, name='list_books'),

    # Library detail view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
