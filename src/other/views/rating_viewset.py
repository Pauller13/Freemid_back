from rest_framework import viewsets
from other.models.rating_model import  RatingModel
from other.serializers.rating_serializer import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializer