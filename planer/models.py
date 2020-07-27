from django.db import models


# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=200)
    floor=models.PositiveIntegerField()
    room_number=models.PositiveIntegerField()

    def __str__(self):
        return  self.name

class Meeting(models.Model):
    title=models.CharField(max_length=200)
    date= models.DateField(default='2020-01-01')
    start_time= models.TimeField(default='00:00:00')
    end_time=models.TimeField(default='00:00:00')
    room=models.ForeignKey(Room, related_name='courses_created', on_delete=models.CASCADE)

    def __str__(self):
        return  self.title