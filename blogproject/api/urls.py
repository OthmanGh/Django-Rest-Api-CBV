from django.urls import path
from .views import BlogPostListCreate, BlogPostRetriveUpdateDestroyAPIView
urlpatterns = [
    path('blogposts/',  BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostRetriveUpdateDestroyAPIView.as_view(), name='blogpost-get-update-delete')
]
