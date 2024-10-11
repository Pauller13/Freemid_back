from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
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


@csrf_exempt  # Désactive la vérification CSRF
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_client_profile(request):
    try:
        client = ClientModel.objects.get(user=request.user)
    except ClientModel.DoesNotExist:
        return JsonResponse({'error': 'Profil du client non trouvé'}, status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        # Utilisation du serializer pour la mise à jour du profil
        serializer = ClientSerializer(client, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

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
    

@csrf_exempt  # Désactive la vérification CSRF
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_freelance_profile(request):
    try:
        # Récupère le profil du freelance lié à l'utilisateur connecté
        freelance = FreelancerModel.objects.get(user=request.user)
    except FreelancerModel.DoesNotExist:
        return JsonResponse({'error': 'Profil du freelance non trouvé'}, status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        # Utilisation du serializer pour la mise à jour du profil
        serializer = FreelancerSerializer(freelance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)