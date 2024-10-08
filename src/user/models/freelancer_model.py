from django.db import models

from base.helpers.date_time_model import DateTimeModel
from user.models.user_model import UserModel


class FreelancerModel(DateTimeModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='freelancer_profile')
    biography = models.TextField(blank=True)
    skills = models.JSONField(default=list)
    certificates = models.JSONField(default=list)
    portfolio = models.JSONField(default=list)
    verification_status = models.BooleanField(default=False)
    rate_card = models.JSONField(default=dict)

    def __str__(self):
        return self.user.username

    @property
    def average_rating(self):
        ratings = self.user.ratings_received.all()
        return ratings.aggregate(models.Avg('score'))['score__avg'] or 0.0