import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EstoqueConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Conecta o cliente ao grupo de WebSocket
        await self.channel_layer.group_add("estoque_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Desconecta o cliente do grupo
        await self.channel_layer.group_discard("estoque_updates", self.channel_name)

    # Recebe mensagem do grupo
    async def estoque_update(self, event):
        await self.send(text_data=json.dumps(event["message"]))


    async def send_movimentacao(self, event):
        movimentacao = event['message']
        await self.send(text_data=json.dumps({
            'message': {
                'produto_id': movimentacao.get('produto_id'),
                'usuario_id': movimentacao.get('usuario_id'),
                'tipo': movimentacao.get('tipo'),
                'data': movimentacao.get('data')
            }
        }))

