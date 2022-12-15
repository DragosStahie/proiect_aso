from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def new_room(request, slug):
    if len(Room.objects.filter(name = slug)) == 0:
        Room.objects.create(name=slug, slug=slug)

    return rooms(request)


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
