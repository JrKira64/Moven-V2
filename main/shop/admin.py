from django.contrib import admin

# Register your models here.
from .models import *


class RoadtripAdmin(admin.ModelAdmin):
    list_display = ("id","From","to")
admin.site.register(Roadtrip,RoadtripAdmin)