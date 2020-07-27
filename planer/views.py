from django.shortcuts import render , redirect
from .models import Room, Meeting
from .forms import CreationForm
# Create your views here.

def room_list (request):

    return render(request, 'room_list.html', {"rooms": Room.objects.all()})

def Meeting_list (request):

    return render(request, 'Meeting_list.html', {"Meetings": Meeting.objects.all()})

def Meeting_room_list (request, r_id):

    room_mmets=Meeting.objects.filter(room=r_id)


    return render(request, 'Meeting_list.html', {"Meetings":room_mmets})

def meet_create(request):
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/post_details/{form.cleaned_data['title']}")
    else:
        form = CreationForm()
    return render(request, "creation.html", {"form": form})
