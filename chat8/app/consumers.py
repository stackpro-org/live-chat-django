#-----------authentication
import json
from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from . models import Group, Chat
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync

class MySyConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket connected...', event)
        print("Channel Layer......", self.channel_layer) #get default channel layer from a project
        print("Channel name", self.channel_name)# get channel name
        self.group_name = self.scope['url_route']['kwargs']['groupNam']


       # add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(
             self.group_name,   #group name
             self.channel_name)
        
        self.send({
            'type':'websocket.accept'
        })
    
    # def websocket_receive(self, event):
    #     print('Data is server or client',  event['text'])  
    #     print('Data is type',  type(event['text']))  
    #     print('envent', event)
    #     data = json.loads(event['text']) # json str to python Dictionary
    #     print('The user is...',self.scope['user']) # to see who is the user
        

    #     group = Group.objects.get(name = self.group_name)

    #     if self.scope['user'].is_authenticated:      
        
    #         chat = Chat(
    #             content=data['msg'],
    #             group = group
    #         )
    #         chat.save()

    #         # added to the coder group
    #         async_to_sync(self.channel_layer.group_send)(self.group_name, { 
    #             'type': 'chat.message',
    #             'message': event['text']
    #         })
        
    #     else:
    #         self.send({
    #             'type':'websocket.send',
    #             'text': json.dumps({"msg": "Login Reguired"}) # py dic to json str
    #         })
    # def chat_message(self, event):
    #     print('event.....', event)
    #     print('Actual data', event['message'])
    #     print('Actual data type', type(event['message']))

    #     self.send({
    #         'type':'websocket.send',
    #         'text': event['message']
    #     })


    def websocket_receive(self, event):
        print('Data is server or client',  event['text'])  
        print('Data is type',  type(event['text']))  
        print('envent', event)
        data = json.loads(event['text']) # json str to python Dictionary
        print('The user is...',self.scope['user']) # to see who is the user
        

        group = Group.objects.get(name = self.group_name)

        if self.scope['user'].is_authenticated:      
        
            chat = Chat(
                content=data['msg'],
                group = group
            )
            chat.save()

            print('dic data1.....', data)
            
            #here in data dic, we added a new element named user
            data['user'] = self.scope['user'].username 
            
            print('dic data2.....', data)

            # added to the coder group
            async_to_sync(self.channel_layer.group_send)(self.group_name, { 
                'type': 'chat.message',
                # 'message': event['text'],
                'message': json.dumps(data) # py dic to json str
            })
        
        else:
            self.send({
                'type':'websocket.send',
                'text': json.dumps({"msg": "Login Reguired"}) # py dic to json str
            })
    def chat_message(self, event):
        print('event.....', event)
        print('Actual data', event['message'])
        print('Actual data type', type(event['message']))

        self.send({
            'type':'websocket.send',
            'text': event['message']
        })



    def websocket_disconnect(self, event):
        print('websocket disconnected...', event)
        print("Channel Layer......", self.channel_layer)
        print("Channel name", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
             self.group_name,   #group name
             self.channel_name)
        raise StopConsumer()

      


class MyAsyConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('websocket connected...', event)
        print("Channel Layer......", self.channel_layer) #get default channel layer from a project
        print("Channel name", self.channel_name)# get channel name
        self.group_name = self.scope['url_route']['kwargs']['groupNam']
        print('scope..................',self.group_name)

       # add a channel to a new or existing group
        await self.channel_layer.group_add(
            self.group_name,   #group name
            self.channel_name)
        
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print('Data is server or client',  event['text'])  
        print('Data is server or client',  type(event['text']))  

        data = json.loads(event['text']) # json str to python Dictionary
        print('The user is...',self.scope['user']) # to see who is the user
        
        
        group = await database_sync_to_async(Group.objects.get)(name = self.group_name)
        if self.scope['user'].is_authenticated:
            chat = Chat(
                content=data['msg'],
                group = group
            )
            await database_sync_to_async(chat.save)() 

            data['user'] = self.scope['user'].username

            # added to the coder group
            await self.channel_layer.group_send(self.group_name, { 
                'type': 'chat.message',
                'message': json.dumps(data)
            })
        else:
            await self.send({
                'type':'websocket.send',
                'text': json.dumps({"msg": "Login Reguired"}) # py dic to json str
            })
    async def chat_message(self, event):
        print('event.....', event)
        print('Actual data', event['message'])
        print('Actual data type', type(event['message']))

        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })
         
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected...', event)
        print("Channel Layer......", self.channel_layer)
        print("Channel name", self.channel_name)
        await self.channel_layer.group_discard(
             self.group_name,   #group name
             self.channel_name)
        raise StopConsumer()

      
