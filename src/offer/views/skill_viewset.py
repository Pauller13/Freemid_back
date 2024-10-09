from  rest_framework import viewsets
from offer.models.skill_models import SkillModel
from offer.serialiazers.skill_serializer import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer