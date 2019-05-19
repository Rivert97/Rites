from django.db import models

class Rider(models.Model):
    id_user = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)

class NoRider(models.Model):
    id_user = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)

class Ride(models.Model):
    id_ride = models.AutoField(primary_key = True)
    host = models.ForeignKey(Rider, on_delete = models.CASCADE)
    starting_point = models.CharField(max_length = 45)
    destination = models.CharField(max_length = 45)
    date = models.DateField()
    hour = models.TimeField()
    room = models.IntegerField()
    n_stops = models.IntegerField()
    cost = models.FloatField()

class Vehicle(models.Model):
    id_vehicle = models.AutoField(primary_key = True)
    user = models.ForeignKey(Rider, on_delete = models.CASCADE)
    model = models.CharField(max_length = 45)
    color = models.CharField(max_length = 45)

class RideGuest(models.Model):
    guest_id = models.AutoField(primary_key = True)
    ride = models.ForeignKey(Ride, on_delete = models.CASCADE)
    user = models.ForeignKey(NoRider, on_delete = models.CASCADE)

class IntermediateStop(models.Model):
    id_stop = models.AutoField(primary_key = True)
    ride = models.ForeignKey(Ride, on_delete = models.CASCADE)
    place = models.CharField(max_length = 45)



