from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from user.models.freelancer_model import FreelancerModel
from user.serializers.freelancer_serialiser import FreelancerSerializer


class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = FreelancerModel.objects.all()
    serializer_class = FreelancerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name', 'user__last_name']
