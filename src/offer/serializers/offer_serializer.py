from rest_framework import serializers
from offer.models.offer_model import OfferModel
from offer.models.skill_model import SkillModel
from offer.serializers.offerskill_serializer import OfferSkillSerializer
from offer.models.offerskill_model import OfferSkillModel


class OfferSerializer(serializers.ModelSerializer):
    required_skills = OfferSkillSerializer(many=True, source="offerskillmodel_set", required=False)

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
        ]

    def create(self, validated_data):
        required_skills_data = validated_data.pop('required_skills', [])
        offer = OfferModel.objects.create(**validated_data)

        for skill_data in required_skills_data:
            skill_name = skill_data['skill']['name']
            skill, _ = SkillModel.objects.get_or_create(name=skill_name)
            OfferSkillModel.objects.create(
                offer=offer,
                skill=skill,
                level_required=skill_data['level_required']
            )

        return offer


    def update(self, instance, validated_data):
        required_skills_data = validated_data.pop('required_skills', [])
        instance = super().update(instance, validated_data)

        # Clear old skills and add new ones
        instance.required_skills.clear()
        for skill_data in required_skills_data:
            skill_name = skill_data['skill']['name']
            skill, _ = SkillModel.objects.get_or_create(name=skill_name)
            OfferSkillModel.objects.create(
                offer=instance,
                skill=skill,
                level_required=skill_data['level_required']
            )

        return instance
