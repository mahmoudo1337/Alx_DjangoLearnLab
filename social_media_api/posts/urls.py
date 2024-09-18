# posts/urls.py

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

post_comment_patterns = [
    path('<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include(post_comment_patterns)),
]
