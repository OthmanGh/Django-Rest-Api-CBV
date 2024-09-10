from .serializers import BlogPostSerializer
from rest_framework import generics
from .models import BlogPost

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

