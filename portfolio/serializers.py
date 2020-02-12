from rest_framework import serializers
from portfolio import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.About
        fields = ('id', 'user_profile', 'Title','text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
        
        
        
class NoteSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.Note
        fields = '__all__'
        