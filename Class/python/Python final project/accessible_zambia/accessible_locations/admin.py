from django.contrib import admin
from .models import AccessibleLocation

@admin.register(AccessibleLocation)
class AccessibleLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'verified', 'has_ramp', 'has_elevator')
    list_filter = ('city', 'verified')
    search_fields = ('name', 'address')
