from rest_framework import routers
from . import views #views.py import
from django.urls import include, path

from .views import PostListAPI, PostDetail

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('post/', PostListAPI.as_view(), basename = 'post') #itemviewset 과 item이라는 router 등록

urlpatterns = [
    path('', PostListAPI.as_view(), name='post'),
    path('detail/', PostDetail, name='post-detail'),
]