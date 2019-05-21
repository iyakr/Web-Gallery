from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from .models import Profile

class UserSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username", "email")

class RegSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( "username", "email", "password")
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
        )
        return user

class RedactSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id","username", "email","role")

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class RedactIMG(serializers.ModelSerializer):
    """Редактирование аватара"""
    class Meta:
        model = Profile
        fields = ("img",)

    def update(self, instance, validated_data):
        instance.img = validated_data.get('img', instance.img)
        instance.save()
        return instance

class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'auth_token')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class RegSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('id', 'email','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    """Сериализация профиля"""
    user = UserSerialiser()
    class Meta:
        model = Profile
        fields = ('id', 'user','img',)

class ProfileRedact(serializers.ModelSerializer):
    user = UserSerialiser()
    class Meta:
        model = Profile
        fields = ( 'user',)

class EditAvatar(serializers.ModelSerializer):
    """Редактирование автара"""
    class Meta:
        model = Profile
        fields = ("id","img", )

class EditEmail(serializers.ModelSerializer):
    """Редактирование email"""
    class Meta:
        model = User
        fields = ("email", )
