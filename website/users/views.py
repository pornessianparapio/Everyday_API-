# users/views.py

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, RegisterSerializer


class LoginView(APIView):
    """
    POST /api/users/login/
    Logs User in!
    {
        "username": "user1",
        "password": "password123"
    }
    """

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)  # This creates a session
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckAuthView(APIView):
    """
    GET /api/users/check-auth/
    Checks if the user is authenticated.
    """
    permission_classes = [

    ]

    def get(self, request, format=None):
        return Response({
            'message': 'User is authenticated',
            'username': request.user.username,
            'roles': {
                'is_admin': request.user.is_admin,
                'is_project_manager': request.user.is_project_manager,
                'is_worker': request.user.is_worker
            }
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    """
    POST /api/users/logout/
    Logs out the user by destroying the session.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    """
    POST /api/users/register/
    {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "newpassword123",
        "password2": "newpassword123",
        "is_admin": false,
        "is_project_manager": true,
        "is_worker": false
    }
    """

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)