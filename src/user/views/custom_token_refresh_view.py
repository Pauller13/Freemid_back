from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.views import TokenRefreshView

from user.models.user_model import UserModel


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data['access']
        # Extraire l'ID de l'utilisateur à partir du token
        try:
            token_data = UntypedToken(access_token)
            user_id = token_data['user_id']
            user = UserModel.objects.get(id=user_id)
        except Exception as e:
            return Response({'detail': 'Invalid token or user not found.'}, status=status.HTTP_401_UNAUTHORIZED)
        response_data = {
            'access': access_token,
            'user_id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
            'photo': user.photo.url if user.photo else None,
        }

        return Response(response_data, status=status.HTTP_200_OK)
