from django import forms
from .models import AccessibleLocation, AccessibilityFeature

class AccessibleLocationForm(forms.ModelForm):
    features = forms.ModelMultipleChoiceField(
        queryset=AccessibilityFeature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = AccessibleLocation
        fields = ['name', 'address', 'latitude', 'longitude', 'features']
