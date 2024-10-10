from rest_framework import serializers
from project.models.payment_model import PaymentModel


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = ["project", "amount", "payment_date", "method", "is_instalment", "instalment_details", "notes"]