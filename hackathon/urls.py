from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from events.views import EventView, EventListView, EventMap

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon.views.home', name='home'),
    # url(r'^hackathon/', include('hackathon.foo.urls')),
    url(r'events/(?P<pk>\d+)/', EventView.as_view(), name="event_detail"),
    url(r'events/$', EventListView.as_view(), name="event_list"),
    url(r'events/map/$', EventMap.as_view(), name="event_map"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
