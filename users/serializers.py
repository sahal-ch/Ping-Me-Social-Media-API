from rest_framework import serializers
from .models import Account
from user_profile.serializers import ProfileSerializer

class UserSerializer(serializers.ModelSerializer) :
    profile_data = ProfileSerializer(read_only=True)
    class Meta :
        model = Account
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'dob', 'gender', 'password', 'is_active', 'profile_data')
        extra_kwargs = {
            'email' : {'required': True, 'write_only': True},
            'password' : {'write_only': True}
        }
        
    def create(self, validated_data) :
        user = Account(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['username'],
            dob = validated_data['dob'],
            gender = validated_data['gender']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user