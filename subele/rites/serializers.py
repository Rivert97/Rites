from rest_framework import serializers
from .models import *
"""
class RiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rider
        fields = '__all__'

class NoRiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoRider
        fields = '__all__'
"""

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id_user', 'first_name', 'last_name')

class RiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id_user', 'first_name', 'last_name', 'rider_score', 'rides_number', 'scored')

class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = '__all__'

class RideFilterSerializer(serializers.ModelSerializer):
    host = UserNameSerializer(read_only=True)
    class Meta:
        model = Ride
        fields = ('host','id_ride','starting_point','destination','date','hour','cost')

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

