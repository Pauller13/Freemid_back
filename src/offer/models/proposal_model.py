from django.db import models

from base.helpers.date_time_model import DateTimeModel
from offer.models.offer_model import OfferModel
from user.models.freelancer_model import FreelancerModel


class ProposalModel(DateTimeModel):
    offer = models.ForeignKey(OfferModel, on_delete=models.CASCADE, related_name='proposals')
    freelancer = models.ForeignKey(FreelancerModel, on_delete=models.CASCADE, related_name='proposals')
    proposed_budget = models.DecimalField(max_digits=10, decimal_places=2)
    proposed_deadline = models.DateTimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Proposal by {self.freelancer} for {self.offer.title}"

    class Meta:
        unique_together = ('offer', 'freelancer')
