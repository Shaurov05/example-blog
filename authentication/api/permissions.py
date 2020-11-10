from rest_framework import permissions
from authentication.models import *

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif not request.user.is_authenticated:
            return False
        else:
            return obj.id == request.user.id
