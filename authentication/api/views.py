from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from authentication.api.serializers import *
from authentication.api.permissions import *
from rest_framework import viewsets
from rest_framework.decorators import action


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from . pagination import StandardResultsSetPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from authentication.api.permissions import IsAuthorOrReadOnly

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get', 'post']


class UserUDRView(RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    authentication_class = JSONWebTokenAuthentication
    serializer_class = UserRegistrationSerializer

    def get_object(self, *args, **kwargs):
        user = get_user_model()
        user = get_object_or_404(user, pk=self.kwargs.get('pk'))
        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        # print("######## put method 1 #########")
        user = self.get_object(pk)
        serializer = UserRegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data["password"]
            same_password = check_password(password, user.password)
            if password != user.password:
                user.set_password(password)
                password = user.password
                confirm_password = password
                serializer.save(password=password, confirm_password=confirm_password)
                return Response(serializer.data)
            else:
                serializer.save()
                return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLoginView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)




#
