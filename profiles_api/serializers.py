from rest_framework import serializers
from .models import UserProfile,ProfileFeedItem

class ProfileFeedSerializer(serializers.ModelSerializer):
     class Meta:
         model=ProfileFeedItem
         fields=('id','user_profile','status_text','created_on',)
         extra_kwargs={
             'user_profile':{
                 'read_only':True,                 
             }
         }

class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('id','name','email','password',)
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        """Create and return new user"""
        user=UserProfile.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password')
        )

        return user