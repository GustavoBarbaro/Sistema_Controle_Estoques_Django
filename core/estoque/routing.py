from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/estoque/', consumers.EstoqueConsumer.as_asgi()),
]
