from rest_framework import serializers
from django.contrib.auth import authenticate
import uuid

from .models import User, Client, Writer



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)

        instance.save()
        if instance.role == User.CLIENT:
            client = Client(
                User=instance,
                client_code=uuid.uuid4().hex
            )
            client.save()
        elif instance.role == User.WRITER:
            client = Client(
                User=instance
            )
            client.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        max_length=20,
        write_only=True,
        required=True
    )
    username = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)

    def create(self, data):
        user = authenticate(username=data.get("email"), password=data.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        return {
            **vars(user),
            "token": user.token
        }




