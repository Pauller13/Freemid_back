from django.db import models

from base.helpers.date_time_model import DateTimeModel
from project.models.project_model import ProjectModel
from user.models.client_model import ClientModel
from user.models.freelancer_model import FreelancerModel


class ConversationModel(DateTimeModel):
    client = models.OneToOneField(ClientModel, on_delete=models.CASCADE)
    freelancer = models.OneToOneField(FreelancerModel, on_delete=models.CASCADE)
    project = models.OneToOneField(ProjectModel, on_delete=models.CASCADE, related_name='conversation', blank=True,
                                   null=True)

    def __str__(self):
        return f"Conversation between {self.client.user.username} and {self.freelancer.user.username}"
