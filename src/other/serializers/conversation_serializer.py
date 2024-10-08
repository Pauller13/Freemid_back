from rest_framework import serializers

from other.models.conversation_model import ConversationModel


class ConversationSerializer(serializers.ModelSerializer):
    client_username = serializers.ReadOnlyField(source='client.user.username')
    freelancer_username = serializers.ReadOnlyField(source='freelancer.user.username')

    class Meta:
        model = ConversationModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']
