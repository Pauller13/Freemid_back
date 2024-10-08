from rest_framework import serializers

from user.models.freelancer_model import FreelancerModel
from user.models.user_model import UserModel
from user.serializers.user_serializer import UserSerializer


class FreelancerSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FreelancerModel
        fields = ['user', 'username', 'biography', 'skills', 'certificates', 'portfolio',
                  'rate_card']
        read_only_fields = ['username', 'verification_status']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserModel.objects.create(**user_data)
        freelancer = FreelancerModel.objects.create(user=user, **validated_data)
        return freelancer
