from django.urls import path
from .views import register, CustomLoginView, profile_view
from .views import PostListView  # Make sure this is present

from django.urls import path
from .views import register, profile_view, CustomLoginView, PostListView

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', PostListView.as_view(), name='list_posts'),  # This should be defined
    # Other URL patterns...
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/new/', PostCreateView.as_view(), name='create_post'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='edit_post'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]


