from django.contrib.auth.models import User
from rest_framework import serializers
from blog import models
# from ..blog.models import *
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'title', 'image', 'like', 'category']

class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        exclude = ['create_dt']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['like']