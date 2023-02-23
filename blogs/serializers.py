from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = ['title', 'thumbnail', 'external_link', 'content', 'blog_type', 'category']