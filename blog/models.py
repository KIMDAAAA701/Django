from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    key = models.AutoField(primary_key=True)

    ID = models.CharField(max_length=200, unique=False, default="abc")
    PW = models.CharField(max_length=200, unique=False, default="123")
