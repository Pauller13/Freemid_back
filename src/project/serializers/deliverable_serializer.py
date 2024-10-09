from rest_framework import serializers
from project.models.deliverable_model import DeliverableModel

class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverableModel
        fields = "__all__"