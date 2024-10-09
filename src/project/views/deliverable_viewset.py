from rest_framework import viewsets
from project.models.deliverable_model import  DeliverableModel
from project.serializers.deliverable_serializer import DeliverableSerializer


class DeliverableViewSet(viewsets.ModelViewSet):
    queryset = DeliverableModel.objects.all()
    serializer_class = DeliverableSerializer