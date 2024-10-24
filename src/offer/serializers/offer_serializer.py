from rest_framework import serializers
from offer.models.offer_model import OfferModel
from offer.serializers.offerskill_serializer import OfferSkillSerializer

from offer.models.offerskill_model import OfferSkillModel


class OfferSerializer(serializers.ModelSerializer):
    required_skills_name = serializers.SerializerMethodField()

    class Meta:
        model = OfferModel
        fields = [
            "id",
            "client",
            "title",
            "description",
            "required_skills",
            "budget",
            "deadline",
            "required_skills_name"
        ]

    def get_required_skills_name(self, obj):
        # Récupérer tous les skills liés à l'offre via OfferSkillModel
        skills = OfferSkillModel.objects.filter(offer=obj)
        return [skill.skill.name for skill in skills]  # Retourner une liste des noms de compétences
