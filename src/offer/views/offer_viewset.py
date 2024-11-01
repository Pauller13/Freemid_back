from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from offer.models.offer_model import OfferModel
from offer.models.offerskill_model import OfferSkillModel
from offer.models.skill_model import SkillModel
from offer.serializers.offer_serializer import OfferSerializer
from user.models.client_model import ClientModel
from django.db import transaction

from user.models.freelancer_model import FreelancerModel


class OfferViewSet(viewsets.ModelViewSet):
    queryset = OfferModel.objects.all()
    serializer_class = OfferSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            client = ClientModel.objects.get(user=request.user)
        except ClientModel.DoesNotExist:
            return Response({'detail': 'Client profile does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['client'] = client.id
        required_skills = data.pop('required_skills', [])
        print(data)
        print(required_skills)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        offer = serializer.save(client=client)

        for skill_data in required_skills:
            skill_name = skill_data.get('skill', {}).get('name')
            skill_name_upper = skill_name.upper()
            level_required = skill_data.get('level_required', '')
            skill, created = SkillModel.objects.get_or_create(name=skill_name_upper)
            OfferSkillModel.objects.create(offer=offer, skill=skill, level_required=level_required)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        try:
            client = ClientModel.objects.get(user=request.user)
        except ClientModel.DoesNotExist:
            return Response({'detail': 'Client profile does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        # Récupérer l'offre à mettre à jour
        offer = self.get_object()
        data = request.data.copy()
        data['client'] = client.id
        required_skills = data.pop('required_skills', [])
        serializer = self.get_serializer(offer, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        offer = serializer.save(client=client)
        # Mettre à jour les compétences requises
        offer.required_skills.clear()
        for skill_data in required_skills:
            skill_name = skill_data.get('skill', {}).get('name')
            skill_name_upper = skill_name.upper()
            level_required = skill_data.get('level_required', '')
            skill, created = SkillModel.objects.get_or_create(name=skill_name_upper)
            OfferSkillModel.objects.create(offer=offer, skill=skill, level_required=level_required)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        # Récupérer le client et le freelance
        try:
            client = ClientModel.objects.get(user=request.user)
        except ClientModel.DoesNotExist:
            return Response({'detail': 'Client  profile does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # Récupérer les offres du client
        client_offers = OfferModel.objects.filter(client=client)
        # Sérialiser les résultats
        client_offer_serializer = OfferSerializer(client_offers, many=True)
        return Response({
            'client_offers': client_offer_serializer.data,
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='list-offers')
    def list_offers(self, request):
        # Récupérer le client et le freelance
        try:
            freelancer = FreelancerModel.objects.get(user=request.user)
        except FreelancerModel.DoesNotExist:
            return Response({'detail': 'Freelancer profile does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)
        freelancer_skills = [skill.upper() for skill in freelancer.skills]

        # Récupérer les offres qui nécessitent des compétences du freelance
        skill_offers = OfferModel.objects.filter(
            offerskillmodel__skill__name__in=freelancer_skills
        ).distinct()
        # Sérialiser les résultats
        skill_offer_serializer = OfferSerializer(skill_offers, many=True)
        return Response({
            'skill_offers': skill_offer_serializer.data
        }, status=status.HTTP_200_OK)
