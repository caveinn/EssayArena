from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(Order.status_choises, required=False)

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
        return order


