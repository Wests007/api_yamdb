from rest_framework import viewsets, generics, permissions, mixins, filters
from rest_framework.views import APIView

from reviews.models import User
from .serializers import UserSerializer


# class CreateListViewSet(mixins.CreateModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     pass
#

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Signup:
    pass
