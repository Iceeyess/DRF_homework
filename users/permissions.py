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

class MyOwn(permissions.BasePermission):
    """class for checking my-own user model"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            print(5, request.user == obj)
            return request.user == obj
        return False

