from django.utils import timezone

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
def post_create(request):
    # reqId = request.id
    # reqPw = request.pw
    reqData = request.data
    # reqData['key'] = int(timezone.now().timestamp())
    serializer = PostSerializer(data=reqData)

    if serializer.is_valid(raise_exception=True):

        # 중복 검사 로직 추가
        id_value =serializer.validated_data.get('ID')
        if Post.objects.filter(id_value=id_value).exists():
            return Response({'error': 'Duplicate ID value'}, status=status.HTTP_400_BAD_REQUEST)
        pw_value = serializer.validated_data.get('PW')
        if Post.objects.filter(pw_value=pw_value).exists():
            return Response({'error': 'Duplicate PW value'}, status=status.HTTP_400_BAD_REQUEST)
        key_value = serializer.validated_data.get('key')
        if Post.objects.filter(key_value=key_value).exists():
            return Response({'error': 'Duplicate key value'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()  # 데이터베이스에 테이블 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)