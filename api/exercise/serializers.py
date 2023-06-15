from rest_framework import serializers
from exercise.models import Exercise
from os import sep


def get_relative_path(obj):
    separated_path = obj.photo.file.name.split(sep)
    relative_path = "/" + "/".join(separated_path[separated_path.index("media") :])
    return relative_path


class ExerciseSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return get_relative_path(obj)

    class Meta:
        model = Exercise
        fields = "__all__"
