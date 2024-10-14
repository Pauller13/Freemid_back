from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from user.models.user_model import UserModel
from user.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    https_methods=['post']
