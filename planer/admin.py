from django.contrib import admin
from .models import Room
from .models import Meeting

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','floor', 'room_number']
    list_filter = ['floor','room_number']
    search_fields = ['name']


@admin.register(Meeting)
class MeetAdmin(admin.ModelAdmin):
    list_display = ['title','date', 'start_time', 'end_time','room']
    list_filter = ['room','date','start_time']
    search_fields = ['title']

