from rest_framework.viewsets import ModelViewSet
from program.serializers import ProgramSerializer
from program.models import Program
from rest_framework.filters import SearchFilter
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
 
        return bool(request.user and request.user.is_staff)

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    search_fields = ['title']
    filter_backends = (SearchFilter,)
    permission_classes = [IsAdminOrReadOnly]