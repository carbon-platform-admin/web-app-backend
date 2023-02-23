from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['name', 'email']
        
    def get_name(self, obj):
        return obj.first_name + ' ' + obj.last_name