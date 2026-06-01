from rest_framework.permissions import BasePermission, SAFE_METHODS

# BasePermission - Базовый класс для своих permissions.
class IsTeacherOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # GET, HEAD, OPTIONS разрешены всем
        if request.method in SAFE_METHODS:
            return True
        
        # Только teacher/admin могут изменять (POST/PUT/DELETE)
        return (
            request.user.is_authentificated and 
            request.user.role in ["teacher", "admin"]
        )
    
