from rest_framework import generics, viewsets,mixins
from django.contrib.auth.models import User
from .models import *
from .serializers import PostSerializer,AddTweetSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render
from .serializers import *

from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

class PostsAll(APIView):
    """Вывод всех постов"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tweets = Post.objects.all()
        paginator = Paginator(tweets,25) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        ordering=['-date']
        ser = PostSerializer(contacts, many=True)
        return Response(ser.data)


class UserPost(APIView):
    """Твиты пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tweets = Post.objects.filter(avtor=request.user)
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = AddTweetSerializer(data=request.data)

        print(request.data.get("id"))
        if ser.is_valid():
            ser.save(avtor=request.user)
            return Response(status=200)
        else:
            return Response(status=400)


    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return Response(status=201)


class PostsDetail(APIView):
    """Вывод поста"""
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(instance=snippet, data=request.data, partial=True)
        if serializer.is_valid():
            if (self.request.user.username == snippet.avtor.username or self.request.user.username == "Administrator"):
                if "image" in request.FILES:
                    serializer.save(image=request.data["image"])
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
            post = self.get_object(pk)
            if (self.request.user.username == post.avtor.username or self.request.user.username == "Administrator"):
                post.delete()
                return Response(status=204)
            return Response(status=400)