from rest_framework import serializers

from .models import Category


class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'icon_url', 'image_url']

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    # image = serializers.SerializerMethodField(read_only=True)
    # icon = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Category
        fields = ['name', 'icon_url', 'image_url', 'parent', 'children', 'promotional_text']
        
        
    def get_children(self, obj):
        try:
            childCategories = obj.children.all()
        except:
            return []
        serializer = SubCategorySerializer(childCategories, many=True)
        return serializer.data
    
    
class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name']