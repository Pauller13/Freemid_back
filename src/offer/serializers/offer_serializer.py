from rest_framework import serializers
from offer.models.offer_model import OfferModel
from offer.serializers.offerskill_serializer import OfferSkillSerializer


class OfferSerializer(serializers.ModelSerializer):
    required_skills_name = serializers.StringRelatedField(source="required_skills", read_only=True)

    class Meta:
        model = OfferModel
        fields = ["id", "client", "title", "description", "required_skills", "budget", "deadline",
                  "required_skills_name"]
