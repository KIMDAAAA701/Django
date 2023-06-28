from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from rest_framework.views import APIView
from rest_framework import status

from .serializer import PostSerializer

@api_view(['GET'])
def getPost(request):
    reqData = Post.objects.all()
    serializer = PostSerializer(reqData, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def post_create(self, request):
    # reqId = request.id
    # reqPw = request.pw
    reqData = request.data
    serializer = PostSerializer(data=reqData)

    if serializer.is_valid(raise_exception=True):
        serializer.save() # 데이터베이스에 테이블 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)