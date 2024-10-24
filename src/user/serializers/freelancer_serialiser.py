from rest_framework import serializers
import base64
from django.core.files.base import ContentFile
from user.models.freelancer_model import FreelancerModel
from user.models.user_model import UserModel
from user.serializers.user_serializer import UserSerializer


class FreelancerSerializer(serializers.ModelSerializer):
    user = UserSerializer(partial=True)

    class Meta:
        model = FreelancerModel
        fields = ['id', 'user', 'biography', 'skills', 'certificates', 'portfolio',
                  'rate_card']
        read_only_fields = ['verification_status']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        if 'photo' in user_data:
            if user_data['photo'] is not None:
                photo_data = user_data['photo']
                if isinstance(photo_data, str) and photo_data.startswith('data:image/'):
                    format, imgstr = photo_data.split(';base64,')
                    ext = format.split('/')[-1]  # obtenir l'extension
                    instance.user.photo.save(f'profile_photo.{ext}', ContentFile(base64.b64decode(imgstr)), save=True)

        # Mettre à jour les champs de l'utilisateur
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Mettre à jour les champs du freelancer
        instance.biography = validated_data.get('biography', instance.biography)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.certificates = validated_data.get('certificates', instance.certificates)
        instance.portfolio = validated_data.get('portfolio', instance.portfolio)
        instance.rate_card = validated_data.get('rate_card', instance.rate_card)

        instance.save()
        return instance

    def validate(self, data):
        # Remove password and confirm_password validation for updates
        if self.instance is not None:  # This is an update
            user_data = data.get('user', {})
            user_data.pop('password', None)
            user_data.pop('confirm_password', None)
        return data
