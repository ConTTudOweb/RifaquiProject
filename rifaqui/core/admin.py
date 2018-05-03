from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Raffle)
class RaffleModelAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    list_display = ('description', 'numbers', 'initial_number')
    save_on_top = True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['numbers', 'initial_number']
        else:
            return []

    class TicketInlineModelAdmin(admin.TabularInline):
        model = Ticket
        extra = 0
        autocomplete_fields = ('client',)
    inlines = [TicketInlineModelAdmin]
