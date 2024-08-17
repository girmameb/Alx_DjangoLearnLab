from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Login view with a custom template
    path('login/', auth_views.LoginView.as_view(template_name='register.html'), name='login'),

    # Logout view with redirect to login page
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),


    # Registration view
    path('register/', register(template_name='register.html'), name='register'),

    # Books list view
    path('books/', list_books, name='list_books'),

    # Library detail view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
