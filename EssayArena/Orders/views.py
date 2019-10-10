from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, Bid
from rest_framework.permissions import AllowAny
from .serializers import OrderSerializer, BidSerializer
from EssayArena.core.permissions import IsClient, IsOwnerOrReadOnly, IsWriter
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
            f'order_{order.id}',
            {
                "type": "update_order",
                'order': serializer.data
            }
        )
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.serializer_class(order)
        order.delete()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'order_{order.id}',
            {
                "type": "delete_order",
                'order': serializer.data
            }
        )
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' \
                or self.action == 'partial_update' or self.action == 'delete':
            permission_classes = [IsClient, IsOwnerOrReadOnly]
        else:
            permission_classes = [AllowAny]
        return [permision() for permision in permission_classes]


class BidViewSet(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = (IsOwnerOrReadOnly, IsWriter)

    def create(self, request, *args, **kwargs):
        order = Order.objects.get(kwargs['order_pk'])
        data = request.data
        data.update({'bidder': request.user.pk, "order": order.id})
        if order.is_to_take:
            data['status'] = Bid.ACCEPTED
            order.status = Order.ASSIGNED
            order.save()

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        bid = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send(
            f'order/{order.id}/bids/{bid.id}',
            {
                'type': "create_bid",
                'bid': serializer.data
            }
        ))
        return Response(serializer.data)


