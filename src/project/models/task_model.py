from django.db import models

from base.helpers.date_time_model import DateTimeModel
from project.models.project_model import ProjectModel
from user.models.user_model import UserModel


class TaskModel(DateTimeModel):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=50, default='Pending')
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_tasks')

    def __str__(self):
        return f"Task for {self.project.offer.title}: {self.description}"
