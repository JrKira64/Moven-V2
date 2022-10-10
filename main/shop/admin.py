from django.contrib import admin

# Register your models here.
from .models import *


class RoadtripAdmin(admin.ModelAdmin):
    list_display = ("id","From","to")
admin.site.register(Roadtrip,RoadtripAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","created_at","contacted","roadtrip","contact")
admin.site.register(Booking,BookingAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","name","email")
admin.site.register(Contact,ContactAdmin)