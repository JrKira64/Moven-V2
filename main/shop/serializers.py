from rest_framework import serializers
from .models import *

class RoadtripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roadtrip
        fields = "__all__"
        depth = 1