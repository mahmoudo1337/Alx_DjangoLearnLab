# posts/urls.py

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import FeedView
from .views import LikePostView, UnlikePostView
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

post_comment_patterns = [
    path('<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include(post_comment_patterns)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
