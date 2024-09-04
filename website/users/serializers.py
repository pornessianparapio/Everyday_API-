# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include `username` and `password`.")

        return data






class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    is_admin = serializers.BooleanField(required=False)
    is_project_manager = serializers.BooleanField(required=False)
    is_worker = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'is_admin', 'is_project_manager', 'is_worker']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_admin=validated_data.get('is_admin', False),
            is_project_manager=validated_data.get('is_project_manager', False),
            is_worker=validated_data.get('is_worker', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
