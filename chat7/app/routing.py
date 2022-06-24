from django.urls import path
from . import consumers

websocket_urlpatterns = [

    path('ws/ac/<str:groupNam>/', consumers.MyAsyConsumer.as_asgi()),
    path('ws/sy/<str:groupNam>/', consumers.MySyConsumer.as_asgi()),
]