from rest_framework import routers
from . import views #views.py import
from django.urls import include, path

router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('Post', views.PostListAPI) #itemviewset 과 item이라는 router 등록

urlpatterns = [
    path('', include(router.urls))
]