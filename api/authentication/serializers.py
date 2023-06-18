from rest_framework import serializers
from authentication.models import User
from program.serializers import ProgramSerializer
from os import sep


def get_relative_path(obj):
    if obj.photo == "":
        return ""
    separated_path = obj.photo.file.name.split(sep)
    relative_path = "/" + "/".join(separated_path[separated_path.index("media") :])
    return relative_path


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    programs_data = ProgramSerializer(source="programs", many=True, read_only=True)

    def get_photo(self, obj):
        return get_relative_path(obj)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "programs_data",
            "photo",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
