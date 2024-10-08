from rest_framework import serializers

from .user_sezializer import UserSerializer
from ..models.client_model import ClientModel
from ..models.user_model import UserModel


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ClientModel
        fields = ['user', 'user_name', 'company_description', 'project_history']
        read_only_fields = ['user_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserModel.objects.create(**user_data)
        client = ClientModel.objects.create(user=user, **validated_data)
        return client
