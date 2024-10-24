from django.db import models

from base.helpers.date_time_model import DateTimeModel
from user.models.user_model import UserModel


class ClientModel(DateTimeModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='client_profile')
    company_description = models.TextField(blank=True, null=True)
    additional_info = models.JSONField(default=list, null=True)
    verification_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    @property
    def average_rating(self):
        ratings = self.user.ratings_received.all()
        return ratings.aggregate(models.Avg('score'))['score__avg'] or 0.0