from rest_framework import routers
from . import views #views.py import
from django.urls import include, path


urlpatterns = [
    path('post/', views.getPost, name="post"),
    path('post/<str:id>', views.getPost, name="post"),
    path('post-create/', views.post_create, name="post-create"),
]