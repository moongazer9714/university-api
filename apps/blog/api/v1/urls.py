from django.urls import path, include
from .views import CategoryListView, TagListView, BlogListView, BlogRetrieveUpdateDestroyView

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    path('tag-list/', TagListView.as_view()),
    path('blog-list-create/', BlogListView.as_view()),
    path('blog-rud/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view()),
]