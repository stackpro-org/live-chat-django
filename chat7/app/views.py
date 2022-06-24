from django.shortcuts import render
from .models import Chat, Group

# Create your views here.
def index(request, group_name):

    group = Group.objects.filter(name = group_name).first()
    if group:
        chats = Chat.objects.filter(group = group)
    else:
        group = Group(name = group_name)
        group.save()
    context = {
            'groupname': group_name,
            'chats': chats
            }
    return render(request, 'index.html', context=context)