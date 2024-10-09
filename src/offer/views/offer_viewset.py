from rest_framework import viewsets
from offer.models.offer_model import  OfferModel
from offer.serializers.offer_serializer import OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = OfferModel.objects.all()
    serializer_class = OfferSerializer