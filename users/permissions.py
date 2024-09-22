from rest_framework import permissions
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()

