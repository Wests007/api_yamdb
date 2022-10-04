from rest_framework import viewsets, permissions, mixins, filters

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

