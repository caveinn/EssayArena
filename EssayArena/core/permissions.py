from rest_framework import permissions
from EssayArena.Auth.models import User


class IsAdmin(permissions.BasePermission):
    message = 'You need to be an admin to perform this action'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == User.ADMIN


class IsWriter(permissions.BasePermission):
    message = 'You need to be an writer to perform this action'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == User.WRITER


class IsClient(permissions.BasePermission):
    message = 'You need to be a client to perform this action'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == User.CLIENT

