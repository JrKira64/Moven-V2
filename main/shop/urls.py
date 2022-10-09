from django.urls import path,include
from .views import *

urlpatterns = [
    path("roadtrip/",RoadtripView.as_view(),name="roadtrip"),
    path("roadtrip/<int:id>/",RoadtripView.as_view(),name="roadtripdetal"),
]