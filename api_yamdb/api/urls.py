from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (UserViewSet, apisignup, apicode, apitoken,
                    CategoryViewSet, GenreViewSet, ReviewViewSet,
                    CommentViewSet, TitleViewSet)


v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/auth/token/', apitoken),
    path('v1/auth/code/', apicode),
    path('v1/auth/signup/', apisignup),
    path('v1/', include(v1_router.urls)),
]
