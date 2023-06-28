from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    key_value = models.FloatField(verbose_name='key', default=float(timezone.now().timestamp()))
    id_value = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='ID', default='123')
    pw_value = models.CharField(max_length=100, verbose_name='PW', default='adc', unique=False)

    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(default=timezone.now, blank=True)
