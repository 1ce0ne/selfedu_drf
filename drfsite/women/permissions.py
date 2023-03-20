from rest_framework import permissions

# Урок 10: Ограничения доступа (permissions) 
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Read все пользователи, Delete админ
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True    
        return bool(request.user and request.user.is_staff)
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Только для авторов
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user