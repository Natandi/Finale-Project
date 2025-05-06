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
    return render(request, "homepage.html")

from django.shortcuts import render
from .models import AccessibleLocation

def location_list_view(request):
    locations = AccessibleLocation.objects.all()
    return render(request, 'accessible_zambia/accessible_locations/templates/index.html', {'locations': locations})

from .forms import AccessibleLocationForm
from django.shortcuts import redirect

def submit_location_view(request):
    if request.method == 'POST':
        form = AccessibleLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location-list')
    else:
        form = AccessibleLocationForm()
    return render(request, 'accessible_places/submit_location.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
