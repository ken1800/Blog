from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import portfolio.routing

application = ProtocolTypeRouter({
    "websocket" : AuthMiddlewareStack(
        URLRouter(
           portfolio.routing.websocket_urlpatterns
        )
    )
})