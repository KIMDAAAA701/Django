from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from rest_framework.views import APIView
from rest_framework import status

from .serializer import PostSerializer

class PostListAPI(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def PostDetail(request):
    # reqId = request.id
    # reqPw = request.pw
    reqData = request.data
    serializer = PostSerializer(data=reqData)

    if serializer.is_valid(raise_exception=True):
        serializer.save() # 데이터베이스에 테이블 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)
