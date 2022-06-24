from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer


class MySyConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket connected...', event)

        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('Data is ',  event['text'])
    
    def websocket_disconnect(self, event):
        raise StopConsumer()

        print('websocket disconnected...', event)


class MyAsyConsumer(AsyncConsumer):

   async def websocket_connect(self, event):
        print('websocket connected...', event)

        await self.send({
            'type':'websocket.accept'
        })
    
   async def websocket_receive(self, event):

        print('Data is ',  event['text'])
    
   async def websocket_disconnect(self, event):
       raise StopConsumer()

       print('websocket disconnected...', event)