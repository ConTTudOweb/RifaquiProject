from django.views.generic import DetailView

from .models import Ticket


class TicketDetailView(DetailView):
    model = Ticket
