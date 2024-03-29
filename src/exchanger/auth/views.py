from django.contrib.auth import authenticate, login
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserRegistrationView(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='username',
                in_=openapi.IN_HEADER,
                description="Имя пользователя",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='email',
                in_=openapi.IN_HEADER,
                description="Электронная почта",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='password',
                in_=openapi.IN_HEADER,
                description="Пароль",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    def post(self, request, *args, **kwargs):
        data = {
            'username': request.headers.get('username'),
            'email': request.headers.get('email'),
            'password': request.headers.get('password'),
        }

        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='username',
                in_=openapi.IN_HEADER,
                description="Имя пользователя",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='password',
                in_=openapi.IN_HEADER,
                description="Пароль",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    def post(self, request, *args, **kwargs):
        data = {
            'username': request.headers.get('username'),
            'password': request.headers.get('password'),
        }
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user:
                login(request, user)
                response = Response({'detail': 'Success login!'}, status=status.HTTP_200_OK)
                response.set_cookie(key='sessionid', value=request.session.session_key)
                return response
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
