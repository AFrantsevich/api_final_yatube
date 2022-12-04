from rest_framework import routers
from django.urls import include, path


from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


v1_router = routers.DefaultRouter()
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(r'v1/groups', GroupViewSet)
v1_router.register(r'v1/follow', FollowViewSet)
v1_router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename="comment-detail")


urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
