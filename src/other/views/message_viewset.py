from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from other.models.message_model import MessageModel
from other.serializers.message_serializer import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content']
