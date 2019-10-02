from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Blog
from blog.serializers import UserSerializer, GroupSerializer, BlogSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response


# Create your views here.
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer

class ListGroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def create(self, request, *args, **kwargs):
        super(BlogCreateView, self).create(request, args, kwargs)
        response = {"result": request.data}
        return Response(response)

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer