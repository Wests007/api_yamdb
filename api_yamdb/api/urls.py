from rest_framework import routers
from django.urls import include, path

from .views import (UserViewSet,
                    APISignup,
                    APICode,
                    APIToken,
                    CategoryViewSet,
                    GenreViewSet)

v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')
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
