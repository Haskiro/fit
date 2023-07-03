from rest_framework.viewsets import ModelViewSet
from program.serializers import ProgramSerializer
from program.models import Program
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.decorators import action
from exercise.models import Exercise
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


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

    @action(methods=["GET"], detail=False)
    def cached_get_programs(self, request):
        if 'programs' in cache:
            # get results from cache 
            programs = cache.get('product')
            return Response(programs)
        else:
            programs = Program.objects.all()
            data = self.serializer_class(programs, many=True).data
            cache.set(programs, data, timeout=CACHE_TTL)
            return Response(data)

    @action(methods=["POST"], detail=False)
    def add_exercise_to_program(self, request, pk=None):
        data = (request.data,)
        program = Program.objects.get(pk=pk)
        currentData = self.serializer_class(id=pk).data
        for exercise_id in data:
            try:
                if exercise_id not in currentData["exercises"]:
                    exercise = Exercise.objects.get(id=exercise_id)
                    currentData["exercises"].append(exercise)
                else:
                    return Response(
                        {
                            "error": "exercise with id="
                            + str(exercise_id)
                            + " already added"
                        },
                        402,
                    )
            except Exercise.DoesNotExist:
                return Response(
                    {"error": "exercise with id=" + exercise_id + "does not exist"}, 402
                )
        program.exercises.set(currentData["exercises"])
        program.save()

        return Response({"message": "exercises added"}, 201)

    # def add_program_to_user(self, request):
    #     data = request.data
    #     user = request.user
    #     currentData = self.serializer_class(user).data
    #     for program_id in data:
    #         try:
    #             if (program_id not in currentData['programs']):
    #                 program = Program.objects.get(id=program_id)
    #                 currentData['programs'].append(program)
    #             else:
    #                 return Response({"error": "program with id=" + str(program_id) + " already added"}, 402)

    #         except Program.DoesNotExist:
    #             return Response(
    #                 {"error": "program with id=" + program_id + "does not exist"}
    #             )
    #     user.programs.set(currentData['programs'])
    #     user.save()

    #     return Response({"message": "programs added"}, 201)
