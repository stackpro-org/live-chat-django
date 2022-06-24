#-----------websocket api javascript

from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
class MySyConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket connected...', event)

        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('Data is ',  event['text'])

        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text': str(i)
            })
            sleep(1)
    
    
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
        for i in range(10):
           await self.send({
                'type':'websocket.send',
                'text': str(i)
            })
           await asyncio.sleep(1)
    
   async def websocket_disconnect(self, event):
       raise StopConsumer()

       print('websocket disconnected...', event)