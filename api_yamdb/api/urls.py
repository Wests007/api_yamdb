from rest_framework import routers
from django.urls import include, path


from .views import (UserViewSet,
                    APISignup,
                    APICode,
                    APIToken,
                    CategoryViewSet,
                    GenreViewSet,
                    ReviewViewSet,
                    CommentViewSet)

v1_router = routers.DefaultRouter()
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
# Оставил эти урлы, но тут что-то не то.
# Зачем создавать эндпойнты genres/<slug:slug> и categories/<slug:slug>? По идее вьюсет это делает сам.
# Так же не совсем ясно зачем в качестве basename указываем ...ViewSet?
# По идее basename это то имя, которое будет в урле при доступе к эндпойнту.
# На мой взгляд правильнее basename указан для эндпойнтов выше.
v1_router.register('categories', CategoryViewSet, basename=CategoryViewSet)
v1_router.register('genres', GenreViewSet, basename=GenreViewSet)
v1_router.register('categories/<slug:slug>', CategoryViewSet, basename=CategoryViewSet)
v1_router.register('genres/<slug:slug>', GenreViewSet, basename=GenreViewSet)

urlpatterns = [
    path('v1/auth/token/', APIToken),
    path('v1/auth/code/', APICode),
    path('v1/auth/signup/', APISignup),
    path('v1/', include(v1_router.urls)),
]
