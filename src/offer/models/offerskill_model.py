from django.db import models

from offer.models.offer_model import OfferModel
from offer.models.skill_model import SkillModel


class OfferSkillModel(models.Model):
    offer = models.ForeignKey(OfferModel, on_delete=models.CASCADE)
    skill = models.ForeignKey(SkillModel, on_delete=models.CASCADE)
    level_required = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.skill.name} (Level: {self.level_required}) required for {self.offer.title}"