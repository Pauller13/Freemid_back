from rest_framework import viewsets, status, filters
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as filters

from user.filters.freelancer_filter import FreelancerFilter
from user.models.freelancer_model import FreelancerModel
from user.serializers.freelancer_serialiser import FreelancerSerializer


class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = FreelancerModel.objects.all()
    serializer_class = FreelancerSerializer
    filter_backends = [SearchFilter, filters.DjangoFilterBackend, ]
    search_fields = ['user__first_name', 'user__last_name', 'skills']
    filterset_class = FreelancerFilter


    def update(self, request, *args, **kwargs):
        return Response({"detail": "PUT method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "PATCH method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['patch'], url_path='update-profile')
    def update_profile(self, request):
        # Récupérer le client associé à l'utilisateur connecté
        freelancer = FreelancerModel.objects.get(user=request.user)
        user_data = request.data.get('user', {})

        # Ne pas valider le username si aucun changement
        if 'username' in user_data:
            if user_data['username'] == freelancer.user.username:
                user_data.pop('username')  # Supprimer le username pour éviter l'erreur

        serializer = self.get_serializer(freelancer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='my-profile')
    def retrieve_client_profile(self, request):
        if request.user.role != 'freelancer':  # Remplacez cette condition par la logique exacte pour vérifier le rôle
            raise PermissionDenied(detail="Vous n'avez pas l'autorisation d'accéder au profil freelancer.")
        # Retrieve the client's profile for the logged-in user
        freelancer = FreelancerModel.objects.get(user=request.user)



        # Mettre à jour le client avec les données fournies
        serializer = self.get_serializer(freelancer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

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