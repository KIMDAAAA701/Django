from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now, blank=True, primary_key=True)
    id = models.CharField(max_length=100, verbose_name='ID', default='123')
    pw = models.CharField(max_length=100, verbose_name='PW', default='adc')

    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(default=timezone.now, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.id