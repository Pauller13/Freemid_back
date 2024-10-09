from rest_framework import viewsets
from project.models.task_model import  TaskModel
from project.serializers.task_serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer