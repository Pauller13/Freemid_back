from rest_framework import serializers
from .user_serializer import UserSerializer
from ..models.client_model import ClientModel
import base64
from django.core.files.base import ContentFile

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(partial=True)  # Allow partial updates

    class Meta:
        model = ClientModel
        fields = ['id','user', 'company_description', 'additional_info']
        read_only_fields = ['verification_status']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        print(user_data)
        user = instance.user

        if 'photo' in user_data:
            if user_data['photo'] is not None:
                photo_data = user_data['photo']
                if isinstance(photo_data, str) and photo_data.startswith('data:image/'):
                    format, imgstr = photo_data.split(';base64,')
                    ext = format.split('/')[-1]  # obtenir l'extension
                    instance.user.photo.save(f'profile_photo.{ext}', ContentFile(base64.b64decode(imgstr)), save=True)

        # Update user fields
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Update client fields
        instance.company_description = validated_data.get('company_description', instance.company_description)
        instance.additional_info = validated_data.get('additional_info', instance.additional_info)

        instance.save()
        return instance

    # def validate(self, data):
    #     # Remove password and confirm_password validation for updates
    #     if self.instance is not None:  # This is an update
    #         user_data = data.get('user', {})
    #         user_data.pop('password', None)
    #         user_data.pop('confirm_password', None)
    #     return data
