from django.contrib.gis import admin
from models import Event,Category

class CategoryInline(admin.TabularInline):
    model = Category


class EventAdmin(admin.OSMGeoAdmin):
    #default_lat = 53.916
    #default_lon = -122.75
    default_lat = 7154263
    default_lon = -13664467
    default_zoom = 12

admin.site.register(Event, EventAdmin)
admin.site.register(Category)
