from rest_framework import permissions
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        print(3, request.user.groups.filter(name='moderators').exists())
        return request.user.groups.filter(name='moderators').exists()

    def has_object_permission(self, request, view, obj):
        print(4, request.user.groups.filter(name='moderators').exists())
        return request.user.groups.filter(name='moderators').exists()

class IsCanEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj
