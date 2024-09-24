from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # if hasattr(view, 'get_object'):
        # obj = view.get_object()
        print(1, request.user == view.queryset.model.objects.get(pk=view.kwargs.get('pk')).owner)
        return request.user == view.queryset.model.objects.get(pk=view.kwargs.get('pk')).owner

    def has_object_permission(self, request, view, obj):
        print(2, request.user == obj.owner)
        return request.user == obj.owner