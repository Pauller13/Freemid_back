from rest_framework import viewsets

from user.models.user_model import UserModel
from user.serializers.user_sezializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
