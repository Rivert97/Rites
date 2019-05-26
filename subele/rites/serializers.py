from rest_framework import serializers
from .models import *

class RiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rider
        fields = '__all__'

class NoRiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoRider
        fields = '__all__'

class RideAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = '__all__'

class RideFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = ('host','starting_point','destination','date','hour')

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

class RideGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideGuest
        fields = '__all__'

class IntermediateStopSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntermediateStop
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
