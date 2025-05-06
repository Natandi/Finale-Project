from django.urls import path
from .views import AccessibleLocationListCreate, AccessibleLocationDetail, home_page, location_list_view

urlpatterns = [
    path('', home_page),
    path('locations/list/', location_list_view, name='location_list'),
    path('locations/', AccessibleLocationListCreate.as_view()),
    path('locations/<int:pk>/', AccessibleLocationDetail.as_view()),
]
