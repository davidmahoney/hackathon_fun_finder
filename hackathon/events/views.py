# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView
import models

class EventView(DetailView):
    template_name = "events/event_detail.html"
    model = models.Event

class EventListView(ListView):
    template_name = "events/event_list.html"
    model = models.Event
