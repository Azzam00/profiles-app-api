from rest_framework import serializers

from profiles_api import models


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializers(serializers.ModelSerializer):
    """Serilazes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','username', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    

    def create(self, validated_data):
        """Create new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user