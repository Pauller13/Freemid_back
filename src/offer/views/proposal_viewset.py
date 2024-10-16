from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from offer.models.offer_model import OfferModel
from offer.models.proposal_model import ProposalModel
from offer.serializers.proposal_serializer import ProposalSerializer
from user.models.client_model import ClientModel
from user.models.freelancer_model import FreelancerModel


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = ProposalModel.objects.all()
    serializer_class = ProposalSerializer

    # def list(self, request, *args, **kwargs):
    #     # Récupérer toutes les propositions reçues pour les offres du client
    #     user = request.user
    #
    #     try:
    #         # Get the client associated with the authenticated user
    #         client = ClientModel.objects.get(user=user)
    #     except ClientModel.DoesNotExist:
    #         return Response({"detail": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
    #
    #     print("Client:", client)
    #     proposals = ProposalModel.objects.filter(offer__client=client)
    #
    #     serializer = ProposalSerializer(proposals, many=True)
    #     print(serializer.data)
    #
    #     return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='get-proposals')
    def get(self, request, *args, **kwargs):

        offer_id = kwargs.get('pk')
        user = request.user

        try:

            client = ClientModel.objects.get(user=user)
        except ClientModel.DoesNotExist:
            return Response({"detail": "Client not found."}, status=status.HTTP_404_NOT_FOUND)

        try:

            offer = OfferModel.objects.get(id=offer_id, client=client)
        except OfferModel.DoesNotExist:
            return Response({"detail": "Offer not found."}, status=status.HTTP_404_NOT_FOUND)

        proposals = ProposalModel.objects.filter(offer=offer)

        serializer = ProposalSerializer(proposals, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        freelancer = FreelancerModel.objects.get(user=request.user)
        data = request.data.copy()
        data['freelancer'] = freelancer.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
