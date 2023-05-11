from rest_framework.viewsets import ModelViewSet
from exercise.serializers import ExerciseSerializer
from exercise.models import Exercise
from rest_framework.filters import SearchFilter

class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    search_fields = ['title']
    filter_backends = (SearchFilter,)
