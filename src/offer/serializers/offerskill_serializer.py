from rest_framework import serializers
from offer.models.offerskill_model import OfferSkillModel


class OfferSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferSkillModel
        fields = ["offer", "skill", "level_required"]