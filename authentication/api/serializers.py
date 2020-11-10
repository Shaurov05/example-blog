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




# class UserRegistrationSerializer(serializers.ModelSerializer):
