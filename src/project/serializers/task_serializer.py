from rest_framework import serializers
from project.models.task_model import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        exclude = ["status"]