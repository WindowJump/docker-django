from channels.generic.websocket import AsyncConsumer


class TestWebSocketConsumer(AsyncConsumer):
    async def websocket_connect(self, scope):
        await self.send({
            'type': 'websocket.accept',
        })
