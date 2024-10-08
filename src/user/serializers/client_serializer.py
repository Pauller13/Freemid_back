from rest_framework import serializers

from .user_sezializer import UserSerializer
from ..models import ClientModel


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ClientModel
        fields = ['user','user_name', 'company_description', 'project_history']
        read_only_fields = ['user_name']
