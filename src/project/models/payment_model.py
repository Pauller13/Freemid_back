from django.db import models

from project.models.project_model import ProjectModel


class PaymentModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50, choices=[
        ('PayPal', 'PayPal'),
        ('Stripe', 'Stripe'),
        ('Orange Money', 'Orange Money'),
        ('Moov Money', 'Moov Money'),
        ('Wave', 'Wave'),
        ('MTN Money', 'MTN Money')
    ])  # Méthode de paiement
    is_instalment = models.BooleanField(default=False)  # Indique si le paiement est échelonné
    instalment_details = models.JSONField(blank=True, null=True)  # Détails des paiements échelonnés
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.project.offer.title} via {self.method}"


