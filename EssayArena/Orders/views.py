from rest_framework.viewsets import  ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from EssayArena.core.permissions import IsAdmin, IsClient
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class OrderViewset(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        data = request.data
        serializer = self.serializer_class(order, data=data, partial=kwargs['partial'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_trial',
            {
                "type": "update_order",
                'order': serializer.data
            }
        )
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsClient]
        else:
            permission_classes = [IsAuthenticated]
        return [permision() for permision in permission_classes]
