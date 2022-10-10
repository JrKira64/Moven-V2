from rest_framework import serializers
from .models import *

class RoadtripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roadtrip
        fields = "__all__"
        depth = 1

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        depth = 1

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        depth = 1