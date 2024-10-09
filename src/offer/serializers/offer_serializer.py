from rest_framework import serializers
from offer.models.offer_model import OfferModel

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferModel
        fields = ["client","title", "description", "required_skills", "budget", "deadline", "specific_requirements"]