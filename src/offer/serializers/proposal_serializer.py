from  rest_framework import serializers
from offer.models.proposal_model import ProposalModel


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalModel
        fields = ["offer","freelancer", "proposed_budget", "proposed_deadline", "message", "is_accepted"]