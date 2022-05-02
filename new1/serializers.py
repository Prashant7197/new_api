
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    class Meta:
        model = User
        fields = ['id', 'title', 'username', 'email', 'groups']
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = User