from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.db.models import Q
from ...models import Blog, Category, Tag
from .serializers import BlogSerializer, CategorySerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly


class CategoryListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/category-list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/tag-list/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogListView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-list-create/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-rud/<id>/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response({"detail": "deleted"}, status=status.HTTP_204_NO_CONTENT)


