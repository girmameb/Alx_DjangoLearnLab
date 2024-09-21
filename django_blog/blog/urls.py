from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, profile_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),  # This should point to the profile_view in views.py
]


from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]
