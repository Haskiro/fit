from rest_framework import serializers
from authentication.models import User
from program.serializers import ProgramSerializer

class UserSerializer(serializers.ModelSerializer):
    programs_data = ProgramSerializer(source='programs', many=True)
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password', 'first_name', 'last_name', 'programs_data']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance