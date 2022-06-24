from django.urls import path
from . import consumers

websocket_urlpatterns = [

    path('ws/ac/', consumers.MyAsyConsumer.as_asgi()),
    path('ws/sy/', consumers.MySyConsumer.as_asgi()),
]