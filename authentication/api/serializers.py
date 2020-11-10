from rest_framework import serializers
from authentication.models import *
from django.contrib.auth import get_user_model
from django.conf import settings
from authentication.api.serializers import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email',
                   'username', 'password', 'confirm_password')

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        validated_data['confirm_password'] = ""
        return validated_data

    def create(self, validated_data):
        new_user = get_user_model().objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
        )
        print("from serializers.py file ",validated_data["password"])
        new_user.set_password(validated_data["password"])
        new_user.save()
        return new_user




from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import check_password

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        try:
            user = CustomUser.objects.get(email=email)
        except :
            user = CustomUser.objects.get(username=email)
        if user is not None:
            authenticated = check_password(password, user.password)

        if not authenticated or user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }
