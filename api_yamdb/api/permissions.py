from rest_framework import permissions


# Данный пермишен не совсем полный. Он дает разрешение доступа, если запрос находится в SAFE_METHODS.
# Но, разрешение доступа если это автор контента не учитывает.
# Пермишен ниже IsAuthorOrReadOnly данную возможность предоставляет
# Пермишен IsAdminOrReadOnly удаляем?
class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
