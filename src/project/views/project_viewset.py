from rest_framework import viewsets
from project.models.project_model import  ProjectModel
from project.serializers.project_serializer import ProjetSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjetSerializer