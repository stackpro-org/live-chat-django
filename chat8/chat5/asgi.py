
import os
import app.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat3.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(
        app.routing.websocket_urlpatterns
    ))
})
