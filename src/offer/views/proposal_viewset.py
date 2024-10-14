from rest_framework import viewsets
from rest_framework.response import Response

from offer.models.offer_model import OfferModel
from offer.models.proposal_model import ProposalModel
from offer.serializers.proposal_serializer import ProposalSerializer
from user.models.client_model import ClientModel


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = ProposalModel.objects.all()
    serializer_class = ProposalSerializer

    def list(self, request, *args, **kwargs):
        # Récupérer toutes les propositions reçues pour les offres du client
        user = request.user
        client = ClientModel.objects.get(user=user)
        offers = OfferModel.objects.filter(client=client)
        proposals = ProposalModel.objects.filter(offer__in=offers)

        serializer = ProposalSerializer(proposals, many=True)
        return Response(serializer.data)