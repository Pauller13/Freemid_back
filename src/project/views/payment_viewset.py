from rest_framework import viewsets
from project.models.payment_model import PaymentModel
from project.serializers.payment_serializer import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer