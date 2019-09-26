from rest_framework import serializers
from .models import Order, Bid
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(Order.status_choices, required=False)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['ordered_by']

    def create(self, validated_data):
        user = self.context['request'].user
        order = Order(
            status=Order.PENDING,
            ordered_by=user,
            cost=validated_data.get("cost"),
            title=validated_data.get('title'),
            body=validated_data.get('body'),
            files=validated_data.get("files")
        )
        order.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_trial',
            {
                "type": "new_order",
                'order': {
                    **validated_data,
                    "cost": float(validated_data["cost"]),
                    "ordered_by": user.id
                }
            }
        )
        return order


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'
        required_fields = ['bid_price']