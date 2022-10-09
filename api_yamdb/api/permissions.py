from rest_framework import permissions


class AdminRole(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
                user.is_authenticated and user.is_admin
                or user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
                user.is_authenticated and user.is_admin
                or user.is_superuser
        )
