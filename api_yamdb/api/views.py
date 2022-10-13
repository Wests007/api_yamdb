import uuid

from django.db import IntegrityError
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import  AccessToken

from reviews.models import User, Category, Genre, Title, Review, Comment
from .filters import TitleFilter
from .serializers import (UserSerializer, SignupSerializer, TokenSerializer,
                          CategorySerializer, GenreSerializer,
                          TitleListSerializer, TitleCreateSerializer,
                          ReviewSerializer, CommentSerializer, UserSerializerForUser)
from .mixins import CreateListDestroyViewSet
from api_yamdb.settings import ADMIN_EMAIL
from .permissions import (IsAuthor, IsModerator, IsAdmin,
                          IsSuperUser, ReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin|IsSuperUser]
    # filter_backends = (filters.SearchFilter,)
    # filterset_fields = ('username')
    lookup_field = 'username'
    # regex = r'[\w\@\.\+\-]+'
    # search_fields = ('username',)

    @action(
        detail=False, methods=['get', 'patch'],
        url_path='me', url_name='me',
        permission_classes=(IsAuthenticated,)
    )
    def about_me(self, request):
        serializer = UserSerializer(request.user)
        if request.method == 'PATCH':
            if request.user.is_admin:
                serializer = UserSerializer(
                    request.user, data=request.data, partial=True
                )
            else:
                serializer = UserSerializerForUser(
                    request.user, data=request.data, partial=True
                )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

def send_confirmation_code(user):
    confirmation_code = default_token_generator.make_token(user)
    subject = 'Код подтверждения для получения токена'
    message = (f'Спасибо за регистрацию! Ниже Вы найдете код подтверждения '
               f'для получения токена. Ваш логин: {user.username},'
               f'email: {user.email}. Код для токена:{confirmation_code}')
    user_email = [user.email]
    send_mail(subject, message, ADMIN_EMAIL, user_email)
    return str(confirmation_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def apisignup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.confirmation_code = send_confirmation_code(user) 
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def apitoken(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid()
    username = serializer.validated_data['username']
    confirmation_code = serializer.validated_data['confirmation_code']
    user = get_object_or_404(User, username=username)
    if confirmation_code == user.confirmation_code:
        token = str(AccessToken.for_user(user))
        return Response({'token': token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def apicode(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         username = serializer.data['username']
#         email = serializer.data['email']
#         user = get_object_or_404(User, username=username, email=email)
#         send_confirmation_code(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthor|IsModerator|ReadOnly|
                          IsAdmin|IsSuperUser]

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        serializer.save(
            author=self.request.user,
            title=get_object_or_404(Title, id=title_id) 
        )

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthor|IsModerator|ReadOnly|
                          IsAdmin|IsSuperUser]
    
    def perform_create(self, serializer):
        review_id = self.kwargs.get("review_id")
        serializer.save(
            author=self.request.user,
            review=get_object_or_404(Review, id=review_id)
        )

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin|IsSuperUser|ReadOnly]
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('name',)


class GenreViewSet(CreateListDestroyViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsAdmin|IsSuperUser|ReadOnly]
    filter_backends = [filters.SearchFilter]
    lookup_field = 'slug'
    search_fields = ('name', 'slug')


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    # queryset = Title.objects.all().annotate(
    #     Avg('reviews__score')
    # ).order_by('name')
    serializer_class = TitleListSerializer
    permission_classes = [IsAdmin|IsSuperUser|ReadOnly]
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('genre',)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return TitleListSerializer
        return TitleCreateSerializer
