# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/orders/(?P<room_name>\w+)/$', consumers.OrderConsumer),
    re_path(r'ws/bids_/(?P<room_name>\w+)/$', consumers.BidConsumer)

]
