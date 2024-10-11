from rest_framework import mixins,generics
from offer.models.offer_model import  OfferModel
from offer.serializers.offer_serializer import OfferSerializer


class OfferViewSet(mixins.ListModelMixin):
    queryset = OfferModel.objects.all()
    serializer_class = OfferSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ClientOffreListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = OfferSerializer


    def get_queryset(self):
        client = self.request.user.client
        return OfferModel.objects.filter(client=client)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


