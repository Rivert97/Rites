from django.contrib import admin
from . models import *

admin.site.register(User)
#admin.site.register(Rider)
#admin.site.register(NoRider)
admin.site.register(Ride)
admin.site.register(Vehicle)
admin.site.register(RideGuest)
admin.site.register(IntermediateStop)
# Register your models here.
