from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class OrderConsumer(WebsocketConsumer):
    """
    A consumer that allows subscription to order list
    """

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        print(self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def update_order(self, order_obj):
        # Send message to WebSocket
        self.send(text_data=json.dumps(
            order_obj
        ))

    def new_order(self, order_obj):
        self.send(text_data=json.dumps(
            order_obj
        ))




