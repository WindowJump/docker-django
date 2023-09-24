import channels.exceptions
from channels.generic.websocket import AsyncConsumer
from channels.exceptions import StopConsumer


class TestWebSocketConsumer(AsyncConsumer):
    async def websocket_connect(self, scope):
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_disconnect(self, scope):
        await self.send({
            'type': 'websocket.close',
        })

        raise StopConsumer
