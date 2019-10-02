from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Blog