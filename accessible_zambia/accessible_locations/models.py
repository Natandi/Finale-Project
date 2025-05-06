from django.db import models

class AccessibleLocation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    has_ramp = models.BooleanField(default=False)
    has_elevator = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='location_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
