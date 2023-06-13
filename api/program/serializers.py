from rest_framework import serializers
from program.models import Program
from exercise.serializers import ExerciseSerializer
from os import sep


def get_relative_path(obj):
    separated_path = obj.photo.file.name.split(sep)
    relative_path = "/" + "/".join(separated_path[separated_path.index("media") :])
    return relative_path


class ProgramSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    photo_thumbnail = serializers.SerializerMethodField()
    exercises_data = ExerciseSerializer(source="exercises", many=True)

    def get_photo(self, obj):
        return get_relative_path(obj)

    def get_photo_thumbnail(self, obj):
        return get_relative_path(obj)

    class Meta:
        model = Program
        # fields = "__all__"
        exclude = ["exercises"]
