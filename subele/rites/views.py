from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *

class RiderList(APIView):
    def get(self, request):
        riders = Rider.objects.all()
        serializer = RiderSerializer(riders, many=True)
        return Response(serializer.data)

class NoRiderList(APIView):
    def get(self, request):
        no_riders = NoRider.objects.all()
        serializer = RiderSerializer(no_riders, many=True)
        return Response(serializer.data)

class RideList(APIView):
    def get(self, request):
        rides = Ride.objects.all()
        serializer = RiderSerializer(rides, many=True)
        return Response(serializer.data)

class VehicleList(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = RiderSerializer(vehicles, many=True)
        return Response(serializer.data)
        
class RideFilter(APIView):
    def get(self, request):
        queryset = Ride.objects.all()
        query = self.request.query_params
        
        if query:
            if 'hour' in query.keys():
                queryset = queryset.filter(hour=query.get('hour'))
            elif 'starting_point' in query.keys():
                queryset = queryset.filter(starting_point=query.get('starting_point'))
            elif 'destination' in query.keys():
                queryset = queryset.filter(destination=query.get('destination'))
            else :
                queryset = queryset.filter(id_ride = IntermediateStop.objects.get(place=query.get('stop')).ride_)

        serializer = RideSerializer(queryset, many=True)
        return Response(serializer.data)

class RideGuestList(APIView):
    def get(self, request):
        guests = RideGuest.objects.all()
        serializer = RiderSerializer(guests, many=True)
        return Response(serializer.data)

class IntermediateStopList(APIView):
    def get(self, request):
        stops = IntermediateStop.objects.all()
        serializer = RiderSerializer(stops, many=True)
        return Response(serializer.data)

