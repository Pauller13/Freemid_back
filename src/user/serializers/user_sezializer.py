from rest_framework import serializers

from user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name']