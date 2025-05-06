from rest_framework import serializers
from .models import AccessibleLocation

class AccessibleLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibleLocation
        fields = '__all__'
