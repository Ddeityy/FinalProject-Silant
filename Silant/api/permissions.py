from rest_framework import permissions


class CustomCarPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    # object owner OR manager have access
    def has_object_permission(self, request, view, obj):
        if (
            not request.user.is_authenticated  # unauthenticated users handled by serializer
            or obj.buyer.id == request.user.id
            or request.user.groups.filter(name="manager").exists()
            or obj.service_company.id == request.user.id
        ):
            return True
        else:
            return False
