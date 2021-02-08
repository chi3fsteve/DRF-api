from rest_framework import serializers
from blog_front.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'category', 'excerpt', 'content', 'published', 'status')