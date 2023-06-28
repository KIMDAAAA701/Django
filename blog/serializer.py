from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Post        # product 모델 사용
        fields = ('__all__')            # 모든 필드 포함

    # def create(self, data):
    #     return Post.object.create(**data)
    #
    # def update(self, instance, data):
    #     instance.id = data.get('ID', instance.id)
    #     instance.pw = data.get('PW', instance.pw)
    #
    #     instance.save()
    #     return instance