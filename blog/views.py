from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from rest_framework.views import APIView
from rest_framework import generics

from .serializer import PostSerializer


class PostListAPI(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer = PostSerializer