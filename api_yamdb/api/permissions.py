from rest_framework import permissions

from reviews.models import MODERATOR, ADMIN


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsModerator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #return request.user.role == 'moderator'
        return request.user.role == MODERATOR


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #return request.user.role == 'admin'
        return request.user.role == ADMIN


class IsSuperUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
