from django.contrib import admin

from luz.conta.models import Conta


@admin.register(Conta)
class ContasAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'amount_paid', 'mw')
    list_display_links = ('id',)
    ordering = ('date',)
