from rest_framework import routers
from django.urls import include, path

from .views import UserViewSet, APISignup

v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    # path('v1/auth/signup/', Signup.as_view()),
    path('v1/', include(v1_router.urls)),

]
