from rest_framework.viewsets import ModelViewSet
from program.serializers import ProgramSerializer
from program.models import Program
from rest_framework.filters import SearchFilter

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    search_fields = ['title']
    filter_backends = (SearchFilter,)
