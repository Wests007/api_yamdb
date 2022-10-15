from rest_framework import permissions


class IsSuperUserOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return (request.user.is_superuser or
                request.user.is_admin)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAuthorAdminModeratorSuperUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS or
                obj.author == request.user or
                request.user.role == 'admin' or
                request.user.role == 'moderator' or
                request.user.is_superuser)
