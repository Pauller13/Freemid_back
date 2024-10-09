from rest_framework import serializers
from other.models.rating_model import RatingModel

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = "__all__"