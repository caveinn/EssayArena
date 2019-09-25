from rest_framework import serializers
from .models import Order, Application
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
        print(type(user))
        order = Order(
            status=Order.PENDING,
            ordered_by=user,
            cost=validated_data.get("cost"),
            title=validated_data.get('title'),
            body=validated_data.get('body'),
        )
        order.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_trial',
            {
                "type": "new_order",
                'order': {
                    **validated_data,
                    "cost": float(validated_data["cost"])
                }
            }
        )
        return order


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['order', 'applicant']
