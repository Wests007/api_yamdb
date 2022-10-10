from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import UserViewSet, APISignup, APICode, APIToken

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/token/', APIToken),
    path('v1/auth/code/', APICode),
    path('v1/auth/signup/', APISignup),
    path('v1/', include(v1_router.urls)),

]
