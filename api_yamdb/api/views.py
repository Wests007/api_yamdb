from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics, permissions, mixins, filters
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import User, Review
from .serializers import UserSerializer, SignupSerializer, TokenSerializer, ReviewSerializer, CommentSerializer
from api_yamdb.settings import ADMIN_EMAIL
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # пермишн лукап филльтр поиск добавить

    @action(
        detail=False, methods=['get', 'patch'],
        url_path='me', url_name='me',
        # permission_classes=(IsAuthenticated,)
    )
    def about_me(self, request):
        serializer = UserSerializer(request.user)
        if request.method == 'PATCH':
            serializer = UserSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthorOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Пока оставлю тут. Проверю вариант выше, если заработает, то уберу
#
# class ReviewViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Review.objects.all()
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Review.objects.all()
#         review = get_object_or_404(queryset, pk=pk)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


@api_view(['POST'])
# @permission_classes([AllowAny])
def APISignup(request):
    """
    Create user with unique username and email
    then send confirmation code to email
    """
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_confirmation_code(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([AllowAny])
def APIToken(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = serializer.data['username']
    user = get_object_or_404(User, username=username)
    confirmation_code = serializer.data['confirmation_code']
    if not default_token_generator.check_token(user, confirmation_code):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    token = RefreshToken.for_user(user)
    return Response(
        {'token': str(token.access_token)}, status=status.HTTP_200_OK
    )


@api_view(['POST'])
# @permission_classes([AllowAny])
def APICode(request):
    serializer = TokenSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        email = serializer.data['email']
        user = get_object_or_404(User, username=username, email=email)
        send_confirmation_code(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_confirmation_code(user):
    confirmation_code = default_token_generator.make_token(user)
    subject = 'Код подтверждения YaMDb'
    message = f'{confirmation_code} - ваш код для авторизации на YaMDb'
    admin_email = ADMIN_EMAIL
    user_email = [user.email]
    return send_mail(subject, message, admin_email, user_email)
