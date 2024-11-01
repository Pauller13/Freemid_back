from rest_framework import serializers
from offer.models.offerskill_model import OfferSkillModel
from offer.serializers.skill_serializer import SkillSerializer


class OfferSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()
    class Meta:
        model = OfferSkillModel
        fields = ["skill", "level_required"]

