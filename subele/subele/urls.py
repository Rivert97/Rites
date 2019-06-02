"""subele URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rites import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserList.as_view()),
    path('ridesfilter/', views.RideFilter.as_view()),
    path('rides/<int:pk>', views.RideList.as_view()),
     path('rides/', views.RideList.as_view()),
    path('vehicles/', views.VehicleList.as_view()),
    path('vehicles/<int:pk>', views.VehicleList.as_view()),
    path('rideguests/', views.RideGuestList.as_view()), 
    path('rideguests/<int:pk>', views.RideGuestList.as_view()),
    path('intermediatestops/', views.IntermediateStopList.as_view()),
    path('intermediatestops/<int:pk>', views.IntermediateStopList.as_view()),
]
