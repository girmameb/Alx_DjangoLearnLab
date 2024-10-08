# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, list_books, LibraryDetailView
from .views import register, login, logout
from relationship_app import views
from .views import admin_view, librarian_view, member_view
from django.urls import path
from .views import add_book, update_book, delete_book

urlpatterns = [
   
    # Login view with a custom templates
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout view with redirect to login page
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # Registration view
path('registration/', views.register, name='register'),

    # Books list view
    path('books/', list_books, name='list_books'),

    # Library detail view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

path('admin/', views.admin_view, name='admin_view'),
path('member/', member_view, name='member_view'),
path('admin/', admin_view, name='admin_view'),
path('librarian/', views.librarian_view, name='librarian_view'),
path('member/', member_view, name='member_view'),

path('add_book/', add_book, name='add_book'),
path('edit_book/<int:pk>edit/', views.edit_book, name='edit_book'),
path('delete_book/<int:pk>delete/', views.delete_book, name='delete_book'),
]
