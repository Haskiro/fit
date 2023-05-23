from rest_framework.viewsets import ModelViewSet
from program.serializers import ProgramSerializer
from program.models import Program
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.decorators import action
from exercise.models import Exercise
from rest_framework.response import Response


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    search_fields = ["title"]
    filter_backends = (SearchFilter,)
    permission_classes = [IsAdminOrReadOnly]

    @action(methods=["POST"], detail=True)
    def add_exercise_to_program(self, request, pk=None):
        data = request.data
        programs = Program.objects.get(pk=pk)
        for program_id in data:
            try:
                exercise = Exercise.objects.get(id=program_id)
                programs.tracks.add(exercise)
            except Exercise.DoesNotExist:
                return Response(
                    {"error": "exercise with id=" + program_id + "does not exist"}
                )
        programs.save()

        return Response({"message": "exercise added"}, 201)
