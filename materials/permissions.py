from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        print(3)
        if hasattr(view, 'get_object'):
            obj = view.get_object()
            print(request.user == obj.owner)
            return request.user == obj.owner

    def has_object_permission(self, request, view, obj):
        print(4)
        print(request.user == obj.owner)
        return request.user == obj.owner