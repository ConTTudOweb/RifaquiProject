from django.contrib import admin, messages
from django.contrib.admin import SimpleListFilter

from rifaqui.core.forms import RaffleModelForm
from rifaqui.core.mixins import ViewOnSiteMixin
from .models import *


@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Raffle)
class RaffleModelAdmin(admin.ModelAdmin):
    form = RaffleModelForm
    search_fields = ('description',)
    list_display = ('description', 'numbers', 'initial_number')
    save_on_top = True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['numbers', 'initial_number']
        else:
            return []

    # class TicketInlineModelAdmin(admin.TabularInline):
    #     model = Ticket
    #     extra = 0
    #     autocomplete_fields = ('client',)
    # inlines = [TicketInlineModelAdmin]


@admin.register(Ticket)
class TicketModelAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    class RaffleFilter(SimpleListFilter):
        title = Raffle._meta.verbose_name
        parameter_name = 'raffle'

        def lookups(self, request, model_admin):
            raffles = set([r for r in Raffle.objects.filter(draw_date__isnull=True)])
            return [(r.id, r.description) for r in raffles]

        def queryset(self, request, queryset):
            if self.value():
                return queryset.filter(raffle__id__exact=self.value())
            else:
                messages.add_message(request, messages.WARNING, 'Escolha uma '+self.title)
                return queryset.filter(raffle__id__exact=0)

    list_display = ('number', 'client', 'booking_date', 'is_paid', 'view_on_site')
    list_filter = (RaffleFilter, 'is_paid')
    list_editable = ('client', 'booking_date', 'is_paid')
    autocomplete_fields = ('client',)
    save_on_top = True

    def has_add_permission(self, request):
        return False
