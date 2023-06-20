from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
    Allows CRUD only to admin users, and SAFE methods
    to the rest.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
