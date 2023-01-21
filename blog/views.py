from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# vou imoportar minha Model o também a classe que está no serializers.py
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.postobjects.all()[0:4]  ## Responsavel por todos os Posts  // OBS: [0:4] isso é paginação
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

# AQUI NESTA VIEW ESTAMOS TRANSFORMANDO NOSSOS DADOS EM JSON