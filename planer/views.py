from django.shortcuts import render
from .models import Room, Meeting

# Create your views here.
def filter(a,room):
    if a.room == room:
        return 1
    else:
        return 0

def room_list (request):

    return render(request, 'room_list.html', {"rooms": Room.objects.all()})

def Meeting_list (request):

    return render(request, 'Meeting_list.html', {"Meetings": Meeting.objects.all()})

def Meeting_room_list (request, room_name):

    room_mmets=Meeting.objects.all()
    filter(room_mmets,room_name)

    return render(request, 'Meeting_list.html', {"Meetings":room_mmets})