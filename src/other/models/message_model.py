from django.db import models

from base.helpers.date_time_model import DateTimeModel
from other.models.conversation_model import ConversationModel
from user.models.user_model import UserModel


class MessageModel(DateTimeModel):
    conversation = models.ForeignKey(ConversationModel, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    is_file = models.BooleanField(default=False)
    file = models.FileField(upload_to='messages/files/', blank=True, null=True)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.conversation}"