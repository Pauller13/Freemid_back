from rest_framework import viewsets
from offer.models.proposal_model import ProposalModel
from offer.serializers.proposal_serializer import ProposalSerializer


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = ProposalModel.objects.all()
    serializer_class = ProposalSerializer