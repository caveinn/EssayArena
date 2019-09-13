from rest_framework.viewsets import  ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from EssayArena.core.permissions import IsAdmin, IsClient


class OrderViewset(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsClient]
        else:
            permission_classes = [IsAuthenticated]
        return [permision() for permision in permission_classes]
