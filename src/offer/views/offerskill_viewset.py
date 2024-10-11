from rest_framework import viewsets, mixins, generics
from offer.models.offerskill_model import OfferSkillModel
from offer.serializers.offerskill_serializer import OfferSkillSerializer



class OfferSkillViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class =OfferSkillModel
    def get_queryset(self):
        skills = self.request.query_params.getlist('skills')
        return OfferSkillModel.objects.filter(skills=skills).distinct()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)