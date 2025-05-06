from django.urls import path, include
from .views import AccessibleLocationListCreate, AccessibleLocationDetail, home_page, location_list_view, submit_location_view, signup_view

urlpatterns = [
    path('', home_page, name='home'),  # This is for the root URL
    path('locations/list/', location_list_view, name='location_list'),
    path('locations/submit/', submit_location_view, name='submit-location'),
    path('accounts/signup/', signup_view, name='signup'),
    path('locations/', AccessibleLocationListCreate.as_view()),
    path('locations/<int:pk>/', AccessibleLocationDetail.as_view()),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password reset
]

