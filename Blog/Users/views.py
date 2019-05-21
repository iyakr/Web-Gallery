from django.shortcuts import render, redirect
from .form import MyUserReg, ProfileImage,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer, EditAvatar, RegSerializer,  RedactSerialiser, RedactIMG
from rest_framework import permissions, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from django.db.models.signals import post_save

class ProfileUser(APIView):
    """Вывод профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = ProfileSerializer(Profile.objects.get(user=request.user))
        return Response(ser.data)

class RegUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class UpdateProfile(APIView):
    """Редактирование аватара"""
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RedactIMG(instance=snippet, data=request.data, partial=True)
        if serializer.is_valid():
            if "img" in request.FILES:
                serializer.save(img=request.data["img"])
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors,status=400)
        else:
            return Response(serializer.errors,status=400)

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        file_serializer = RedactIMG(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=201)
        else:
            return Response(file_serializer.errors, status=400)

class RedactProfile(APIView):
    """Редактирование профиля"""
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404


    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RedactSerialiser(instance=snippet, data=request.data, partial=True)
        if serializer.is_valid():
            if (self.request.user.username == snippet.username):
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=400)
