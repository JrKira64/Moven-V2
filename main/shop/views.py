# Create your views here.
from rest_framework.response import Response
from rest_framework import views,viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from core.crudview import  CRUDView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class RoadtripView(CRUDView):
   
    queryset = Roadtrip.objects.all().order_by("-id")
    serializer_class=RoadtripSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['From','to','Date']
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, *args, **kwargs):
        RoadtripSerializers.Meta.depth = 0
        data = request.data
        wrappers = super().create(request, *args, **kwargs)
        
        return wrappers


class ContactView(CRUDView):
   
    queryset = Contact.objects.all()
    serializer_class=ContactSerializers

    def post(self, request, *args, **kwargs):
        ContactSerializers.Meta.depth = 0
        data = request.data
        wrappers = super().create(request, *args, **kwargs)
        ContactSerializers.Meta.depth = 1
        return wrappers

class BookingView(CRUDView):
   
    queryset = Booking.objects.all()
    serializer_class=BookingSerializers

    def post(self, request, *args, **kwargs):
        BookingSerializers.Meta.depth = 0
        
        data = request.data
        wrappers = super().create(request, *args, **kwargs)
        BookingSerializers.Meta.depth = 1
        return wrappers
