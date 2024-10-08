from rest_framework import serializers

from user.models.user_model import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']