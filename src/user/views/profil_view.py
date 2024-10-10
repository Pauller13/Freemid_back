from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.serializers.profil_serializer import ProfilSerializer
from user.models.freelancer_model import FreelancerModel
from ..models.client_model import ClientModel
from user.serializers.user_serializer import UserSerializer
from user.models.user_model import UserModel
from user.serializers.freelancer_serialiser import FreelancerSerializer
from user.serializers.client_serializer import ClientSerializer

# @api_view(['GET'])
# def get_user_profile(request):
#     # Récupère l'utilisateur connecté via la session
#     if request.user.is_authenticated:
#         user = request.user
#         serializer = ProfilSerializer(user)
#         return Response(serializer.data)
#     else:
#         return Response({'detail': 'Utilisateur non connecté'}, status=401)

@api_view(['GET'])
def get_current_user_profile(request):
    user = request.user
    if user.is_authenticated:
        # On suppose que le modèle User a une relation OneToOne avec Client ou Freelancer
        try:
            client = ClientModel.objects.get(user=user)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except ClientModel.DoesNotExist:
            try:
                freelancer = FreelancerModel.objects.get(user=user)
                serializer = FreelancerSerializer(freelancer)
                return Response(serializer.data)
            except FreelancerModel.DoesNotExist:
                return Response({'detail': 'Profil non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'detail': 'Utilisateur non connecté'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_clients_profiles(request):
    clients = ClientModel.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_client_profile_by_id(request,id):
    try:
        client = ClientModel.objects.get(id=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    except ClientModel.DoesNotExist:
        return Response({'detail': 'Client non trouvé'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_freelancers_profiles(request):
    freelancers = FreelancerModel.objects.all()
    serializer = FreelancerSerializer(freelancers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_freelancer_profile_by_id(request,id):
    try:
        freelancer = FreelancerModel.objects.get(id=id)
        serializer = FreelancerSerializer(freelancer)
        return Response(serializer.data)
    except FreelancerModel.DoesNotExist:
        return Response({'detail': 'Freelance non trouvé'}, status=status.HTTP_404_NOT_FOUND)