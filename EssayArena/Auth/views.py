from rest_framework.viewsets import  GenericViewSet
from rest_framework.mixins import  CreateModelMixin
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer

from .models import User

# Create your views here.


class RegistrationView(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return user


class LoginAPIView(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        user_data = request.data.get('user', {})
        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        return serializer.data








