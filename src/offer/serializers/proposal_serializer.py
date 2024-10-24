from rest_framework import serializers
from offer.models.proposal_model import ProposalModel
from user.serializers.freelancer_serialiser import FreelancerSerializer


class ProposalSerializer(serializers.ModelSerializer):
    freelancer = FreelancerSerializer(partial=True)
    class Meta:
        model = ProposalModel
        fields = ["offer", "freelancer", "proposed_budget", "proposed_deadline", "message"]
