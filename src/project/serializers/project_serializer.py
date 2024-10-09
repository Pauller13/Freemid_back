from rest_framework import serializers
from project.models.project_model import ProjectModel

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = "__all__"