from django.db import models
from offer.models.offer_model import OfferModel
from user.models.user_model import UserModel


class RatingModel(models.Model):
    rated_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ratings_received')
    rater_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ratings_given')
    offer = models.ForeignKey(OfferModel, on_delete=models.CASCADE, related_name='ratings')
    score = models.FloatField()
    review = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rated_user} rated {self.score} by {self.rater_user} on {self.offer}'