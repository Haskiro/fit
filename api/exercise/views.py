from rest_framework.viewsets import ModelViewSet
from exercise.serializers import ExerciseSerializer
from exercise.models import Exercise
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    search_fields = ["title"]
    filter_backends = (SearchFilter,)
    permission_classes = [IsAdminOrReadOnly]
