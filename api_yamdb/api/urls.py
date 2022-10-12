from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (UserViewSet,
                    APISignup,
                    APICode,
                    APIToken,
                    CategoryViewSet,
                    GenreViewSet,
                    ReviewViewSet,
                    CommentViewSet)


v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')
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
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
#v1_router.register('titles', GenreViewSet, basename='titles')

urlpatterns = [
    path('v1/auth/token/', APIToken),
    path('v1/auth/code/', APICode),
    path('v1/auth/signup/', APISignup),
    path('v1/', include(v1_router.urls)),
]
