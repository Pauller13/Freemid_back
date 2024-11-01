from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Obtain the access and refresh tokens
        token = serializer.validated_data
        user = serializer.user  # Get the user instance

        # Build the response with access token and user details
        response_data = {
            'access': token['access'],
            'refresh': token['refresh'],
            'user_id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
            'photo': user.photo.url if user.photo else None
        }

        return Response(response_data)
