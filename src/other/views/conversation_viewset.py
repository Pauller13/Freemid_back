from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from base.filters.name_concat_searchFilter import NameConcatSearchFilter
from other.models.conversation_model import ConversationModel
from other.serializers.conversation_serializer import ConversationSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = ConversationModel.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [NameConcatSearchFilter]
    search_fields = ['client', 'freelancer']
