from rest_framework import generics
from .models import AccessibleLocation
from .serializers import AccessibleLocationSerializer

class AccessibleLocationListCreate(generics.ListCreateAPIView):
    queryset = AccessibleLocation.objects.filter(verified=True)
    serializer_class = AccessibleLocationSerializer

class AccessibleLocationDetail(generics.RetrieveAPIView):
    queryset = AccessibleLocation.objects.all()
    serializer_class = AccessibleLocationSerializer

from django.shortcuts import render

def home_page(request):
    return render(request, "index.html")

from django.shortcuts import render
from .models import AccessibleLocation

def location_list_view(request):
    locations = AccessibleLocation.objects.all()
    return render(request, 'accessible_zambia/accessible_locations/templates/index.html', {'locations': locations})
