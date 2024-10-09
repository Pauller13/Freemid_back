from rest_framework import serializers

from other.models.message_model import MessageModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']
