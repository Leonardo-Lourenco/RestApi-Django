# Convertendo os campos da Model em um arquivo JSON da API

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('id', 'title','thumbnail', 'excerpt', 'content', 'slug', 'published', 'author', 'status')