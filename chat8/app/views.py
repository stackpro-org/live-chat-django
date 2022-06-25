from django.shortcuts import render, redirect
from .models import Chat, Group

# Create your views here.



def index(request, group_name):

    group = Group.objects.get(name = group_name)
    if group:
        chats = Chat.objects.filter(group = group)

        
    context = {
            'groupname': group_name,
            'chats': chats
            }
    return render(request, 'index.html', context=context)

def live_chat(request):


    return render(request, 'live_chat.html')


def home(request):

    group = Group.objects.all()

    context={
        'groups':group,

        }

    return render(request, 'home.html', context)


