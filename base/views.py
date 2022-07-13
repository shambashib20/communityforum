from django.shortcuts import render
from .models import Room

# Create your views here.
# rooms = [
#     {'id':1, 'name':'Lets learn React!'},
#     {'id':2, 'name':'Design with me!'},
#     {'id':3, 'name':'Lets learn Java!'},
#     {'id':4, 'name':'Frontend Development!'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms} 
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
