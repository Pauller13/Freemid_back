from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied

from user.models.client_model import ClientModel
from user.models.user_model import UserModel
from user.serializers.client_serializer import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'project_history']

    def update(self, request, *args, **kwargs):
        return Response({"detail": "PUT method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "PATCH method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['patch'], url_path='update-profile')
    def update_profile(self, request):
        # Récupérer le client associé à l'utilisateur connecté
        client = ClientModel.objects.get(user=request.user)
        user_data = request.data.get('user', {})
        print(user_data, '2')

        # Ne pas valider le username si aucun changement
        if 'username' in user_data:
            if user_data['username'] == client.user.username:
                user_data.pop('username')  # Supprimer le username pour éviter l'erreur
        if 'photo' in user_data:
            user_data['photo'] = user_data['photo']

        serializer = self.get_serializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='my-profile')
    def retrieve_client_profile(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail="Vous n'avez pas l'autorisation d'accéder au profil client.")

        if request.user.role != 'client':
            raise PermissionDenied(detail="Vous n'avez pas l'autorisation d'accéder au profil client.")

        client, created = ClientModel.objects.get_or_create(user=request.user)

        # Optionally initialize default fields for new clients
        if created:
            client.company_description = ''
            client.additional_info = []
            client.save()

        serializer = self.get_serializer(client)
        return Response(serializer.data)

    @action(detail=False, methods=['patch'], url_path='update-password')
    def update_password(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not user.check_password(current_password):
            return Response({"detail": "Mot de passe actuel incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Mot de passe changé avec succès."})
