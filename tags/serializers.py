from rest_framework import serializers

from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ['name', 'icon_url', 'icon_alt_text']