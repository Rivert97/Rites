from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
from datetime import datetime, timedelta
"""
class RiderList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_user' in query.keys():
            saved_rider = get_object_or_404(Rider.objects.all(), pk=query.get('id_user'))
            serializer = RiderSerializer(saved_rider)
        else:
            riders = Rider.objects.all()
            serializer = RiderSerializer(riders, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        rider = request.data
        serializer = RiderSerializer(data=rider)
        if serializer.is_valid(raise_exception=True):
            rider_saved = serializer.save()
        return Response({"success":"Rider '{}' created successfully".format(rider_saved.id_user)})

    def put(self, request, pk):
        saved_rider = get_object_or_404(Rider.objects.all(), pk=pk)
        data = request.data
        serializer = RiderSerializer(instance=saved_rider, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            rider_saved = serializer.save()
        return Response({"success": "Rider '{}' updated successfully".format(rider_saved.id_user)})
    
    def delete(self, request, pk):
        rider = get_object_or_404(Rider.objects.all(), pk=pk)
        rider.delete()
        return Response({"success": "Rider with id `{}` has been deleted.".format(pk)},status=204)

class NoRiderList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_user' in query.keys():
            saved_noRider = get_object_or_404(NoRider.objects.all(), pk=query.get('id_user'))
            serializer = NoRiderSerializer(saved_noRider)
        else:
            no_riders = NoRider.objects.all()
            serializer = NoRiderSerializer(no_riders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        noRider = request.data
        serializer = NoRiderSerializer(data=noRider)
        if serializer.is_valid(raise_exception=True):
            noRider_saved = serializer.save()
        return Response({"success":"NoRider '{}' created successfully".format(noRider_saved.id_user)})

    def put(self, request, pk):
        saved_noRider = get_object_or_404(NoRider.objects.all(), pk=pk)
        data = request.data
        serializer = NoRiderSerializer(instance=saved_noRider, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            noRider_saved = serializer.save()
        return Response({"success": "NoRider '{}' updated successfully".format(noRider_saved.id_user)})
    
    def delete(self, request, pk):
        noRider = get_object_or_404(NoRider.objects.all(), pk=pk)
        noRider.delete()
        return Response({"success": "NoRider with id `{}` has been deleted.".format(pk)},status=204)
"""

class VehicleList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_vehicle' in query.keys():
            vehicle = Vehicle.objects.all().filter(id_vehicle=query.get('id_vehicle'))
            serializer = VehicleSerializer(vehicle,many=True)
        elif 'user' in query.keys():
            vehicle = Vehicle.objects.all().filter(user_id=query.get('user'))
            serializer = VehicleSerializer(vehicle,many=True)
        else:
            vehicles = Vehicle.objects.all()
            serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        vehicle = request.data
        serializer = VehicleSerializer(data=vehicle)
        if serializer.is_valid(raise_exception=True):
            vehicle_saved = serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_vehicle = get_object_or_404(Vehicle.objects.all(), pk=pk)
        data = request.data
        serializer = VehicleSerializer(instance=saved_vehicle, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            vehicle_saved = serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        vehicle = get_object_or_404(Vehicle.objects.all(), pk=pk)
        vehicle.delete()
        return Response({"success": "Vehicle with id `{}` has been deleted.".format(pk)},status=204)
        
class RideFilter(APIView):
    def get(self, request):
        query = self.request.query_params

        queryset = Ride.objects.all()
        day_now = datetime.now().date()
        day_next = day_now + timedelta(days=1)
        time_now = datetime.now().time()
        if query:
            if 'hour' in query.keys():
                queryset = queryset.filter(hour=query.get('hour'), is_active=True)
            elif 'starting_point' in query.keys():
                queryset = queryset.filter(starting_point=query.get('starting_point'), is_active=True)
            elif 'destination' in query.keys():
                queryset = queryset.filter(destination=query.get('destination'), is_active=True)
            else :
                queryset = queryset.filter(id_ride = IntermediateStop.objects.get(place=query.get('stop')).ride_id, is_active=True)

            queryset = queryset.filter(date__range=(day_now,day_next))
            queryset = queryset.exclude(date=day_now,hour__range=("00:00",time_now))
            serializer = RideFilterSerializer(queryset,many=True)
        else:
            queryset = queryset.filter(is_active=True)
            queryset = queryset.filter(date__range=(day_now,day_next))
            queryset = queryset.exclude(date=day_now,hour__range=("00:00",time_now))
            serializer = RideFilterSerializer(queryset, many=True)
            
        return Response(serializer.data)

class RideList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_ride' in query.keys():
            rides = Ride.objects.all().filter(id_ride=query.get('id_ride'), is_active=True)
            serializer = RideSerializer(rides,many=True)
        else:
            rides = Ride.objects.all()
            serializer = RideSerializer(rides, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        ride = request.data
        serializer = RideSerializer(data=ride)
        if serializer.is_valid(raise_exception=True):
            ride_saved = serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_ride = get_object_or_404(Ride.objects.all(), pk=pk)
        data = request.data
        serializer = RideSerializer(instance=saved_ride, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ride_saved = serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        ride = get_object_or_404(Ride.objects.all(), pk=pk)
        ride.delete()
        return Response({"success": "Ride with id `{}` has been deleted.".format(pk)},status=204)

class RideGuestList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_ride' in query.keys():
            saved_guests = RideGuest.objects.all().filter(ride=query.get('id_ride'))
            serializer = RideGuestSerializer(saved_guests, many=True)
        else:
            guests = RideGuest.objects.all()
            serializer = RideGuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        guest = request.data
        serializer = RideGuestSerializer(data=guest)
        if serializer.is_valid(raise_exception=True):
            guest_saved = serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_guest = get_object_or_404(RideGuest.objects.all(), pk=pk)
        data = request.data
        serializer = RideGuestSerializer(instance=saved_guest, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            guest_saved = serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        guest = get_object_or_404(RideGuest.objects.all(), pk=pk)
        guest.delete()
        return Response({"success": "RideGuest with id `{}` has been deleted.".format(pk)},status=204)

class IntermediateStopList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_ride' in query.keys():
            saved_stops = IntermediateStop.objects.all().filter(ride=query.get('id_ride'))
            serializer = IntermediateStopSerializer(saved_stops, many=True)
        else:
            stops = IntermediateStop.objects.all()
            serializer = IntermediateStopSerializer(stops, many=True)
        return Response(serializer.data)

    def post(self, request):
        stop = request.data
        serializer = IntermediateStopSerializer(data=stop)
        if serializer.is_valid(raise_exception=True):
            stop_saved = serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_stop = get_object_or_404(IntermediateStop.objects.all(), pk=pk)
        data = request.data
        serializer = IntermediateStopSerializer(instance=saved_stop, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            stop_saved = serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        stop = get_object_or_404(IntermediateStop.objects.all(), pk=pk)
        stop.delete()
        return Response({"success": "Article with id `{}` has been deleted.".format(pk)},status=204)


class UserList(APIView):
    def get(self, request):
        query = self.request.query_params
        if 'id_user' in query.keys():
            saved_user = get_object_or_404(User.objects.all(), pk=query.get('id_user'))
            serializer = UserSerializer(saved_user)
        elif ("email") and ("password") in query.keys():
            query_set=User.objects.all()
            query_set=query_set.filter( email=query.get("email"), password=query.get("password"))
            serializer=UserSerializer(query_set, many=True)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"success": "User with id `{}` has been deleted.".format(pk)},status=204)

