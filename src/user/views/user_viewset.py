import random
import string

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models.client_model import ClientModel
from user.models.freelancer_model import FreelancerModel
from user.models.user_model import UserModel
from user.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    https_methods = ['post', 'patch']

    def perform_create(self, serializer):
        serializer.save()
        if self.request.data.get('role') == 'freelancer':
            FreelancerModel.objects.create(
                user=serializer.instance,
                biography='',
                skills={},
                certificates=[],
                portfolio={},
                rate_card={},
            )
        elif self.request.data.get('role') == 'client':
            ClientModel.objects.create(
                user=serializer.instance,
                company_description='',
                additional_info=[],
            )


    @action(detail=False, methods=['patch'], url_path='reset-password')
    def reset_password(self, request, *args, **kwargs):
        email = request.data.get('email')

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Générer un mot de passe aléatoire
        new_password = self.generate_random_password()

        # Mettre à jour le mot de passe de l'utilisateur
        user.set_password(new_password)
        user.save()

        # Envoyer un email au propriétaire du compte
        self.send_password_reset_email(user.email, new_password)

        return Response({'detail': 'Password reset successfully, new password sent via email.'},
                        status=status.HTTP_200_OK)

    @staticmethod
    def generate_random_password(length=12):
        """Génère un mot de passe aléatoire."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))

    @staticmethod
    def send_password_reset_email(email, new_password):
        """Envoie un email avec le nouveau mot de passe."""
        subject = 'Password Reset Notification'
        message = f'Your password has been reset to: {new_password}'
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(subject, message, from_email, [email])
