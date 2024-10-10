from django.db import models

from base.helpers.date_time_model import DateTimeModel
from offer.models.proposal_model import ProposalModel


class ProjectModel(DateTimeModel):
    proposal = models.OneToOneField(ProposalModel, on_delete=models.CASCADE, related_name='project')
    status = models.CharField(max_length=50, default='In Progress')
    tasks_enabled = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=50, default='Pending')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_steps = models.JSONField(blank=True, null=True)
    rating_client = models.IntegerField(blank=True, null=True)
    rating_freelancer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Project for {self.offer.title} by {self.freelancer.user.username}"