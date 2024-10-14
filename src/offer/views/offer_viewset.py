from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from offer.models.offer_model import OfferModel
from offer.models.offerskill_model import OfferSkillModel
from offer.serializers.offer_serializer import OfferSerializer
from user.models.client_model import ClientModel
from django.db import transaction


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

        required_fields = ['title', 'description', 'budget', 'deadline', 'required_skills']
        for field in required_fields:
            if field not in data or data[field] is None:
                return Response({field: ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        required_skills = data.pop('required_skills')
        print("Required Skills:", required_skills)

        if not required_skills:
            return Response({"required_skills": ["At least one skill is required."]},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            offer = serializer.save(client=client)

            skill_ids = []
            for skill_data in required_skills:
                skill_id = skill_data.get('skill', {}).get('id')

                try:
                    OfferSkillModel.objects.create(
                        offer=offer,
                        skill_id=skill_id,
                        level_required=skill_data.get('level_required', '')
                    )
                    skill_ids.append(skill_id)
                except Exception as e:
                    offer.delete()
                    print("Error creating OfferSkillModel:", str(e))
                    return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            offer.required_skills.set(skill_ids)
            offer.refresh_from_db()

            # Reserialize the offer to include associated skills
            serializer = self.get_serializer(offer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
