from django.db import models

from project.models.project_model import ProjectModel


class DeliverableModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='deliverables')
    file = models.FileField(upload_to='deliverables/')  # Fichier soumis
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  # Statut d'approbation du livrable

    def __str__(self):
        return f"Deliverable for {self.project.offer.title}: {self.file.name}"