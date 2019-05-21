# posts/serializers.py
from rest_framework import serializers
from . import models
from .models import Post
from Users.models import Profile
from django.contrib.auth.models import User


class UserSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")

class ProfileSer(serializers.ModelSerializer):
    user=UserSerialiser()
    class Meta:
        model = Profile
        fields = ("user", "img")


class PostSerializer(serializers.ModelSerializer):
    avtor=UserSerialiser()
    # comment=CommentSerializer( many=True)
    class Meta:
        model = Post
        fields = ('id', 'title','text', 'date', 'avtor', 'image')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.avtor = validated_data.get('avtor', instance.avtor)
        instance.date = validated_data.get('date', instance.date)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance



class AddTweetSerializer(serializers.ModelSerializer):
    """Добавление поста"""

    class Meta:
        model = Post
        fields = ("title","text","image")

# class AddCommentSerializer(serializers.ModelSerializer):
#     """Добавление поста"""
#
#     class Meta:
#         model = Comment
#         fields = ("text",)
