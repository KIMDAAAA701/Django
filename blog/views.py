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

    basename = 'PostDetail'  # 원하는 basename을 지정하세요

    def get_queryset(self):
        # 원하는 queryset을 동적으로 반환하는 로직을 작성하세요
        return Post.objects.id  # 원하는 조건에 맞게 queryset을 필터링하거나 정렬하세요