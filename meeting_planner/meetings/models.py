from datetime import time

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: on {self.floor}: room{self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField(default=time(8))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: on {self.date}: start_time{self.start_time}: duration {self.duration}"

