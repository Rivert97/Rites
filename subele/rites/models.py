from django.db import models

class User(models.Model):
    id_user=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=20)


class Rider(models.Model):
    id_user = models.OneToOneField(
        User,
        unique=True,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    score=models.IntegerField(default=0)
    rides_number=models.IntegerField()
    scored=models.IntegerField()


class NoRider(models.Model):
    id_user = models.OneToOneField(
        User,
        unique=True,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    score=models.IntegerField(default=0)
    rides_number=models.IntegerField()
    scored=models.IntegerField()


class Vehicle(models.Model):
    id_vehicle = models.AutoField(primary_key = True)
    user = models.ForeignKey(Rider, on_delete = models.CASCADE)
    model = models.CharField(max_length = 45)
    color = models.CharField(max_length = 45)
    plates=models.CharField(max_length=20)


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
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class IntermediateStop(models.Model):
    id_stop = models.AutoField(primary_key = True)
    ride = models.ForeignKey(Ride, on_delete = models.CASCADE)
    place = models.CharField(max_length = 45)


class RideGuest(models.Model):
    guest_id = models.AutoField(primary_key = True)
    ride = models.ForeignKey(Ride, on_delete = models.CASCADE)
    user = models.ForeignKey(NoRider, on_delete = models.CASCADE)