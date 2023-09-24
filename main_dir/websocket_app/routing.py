from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/websocket_test/', consumers.TestWebSocketConsumer.as_asgi()),
]
