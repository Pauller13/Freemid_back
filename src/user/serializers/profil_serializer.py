from rest_framework import serializers

from user.models.user_model import UserModel




class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [ 'username', 'email', 'first_name', 'last_name']

