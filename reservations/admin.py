from django.contrib import admin
from reservations.models import InternationalReservation,DomesticReservation
# Register your models here.

@admin.register(InternationalReservation)
class InternationalReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'destination', 'travel_date')
    search_fields = ('name', 'email', 'destination')
    list_filter = ('destination', 'travel_date')

@admin.register(DomesticReservation)
class DomesticReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'destination', 'travel_date')
    search_fields = ('name', 'email', 'destination')
    list_filter = ('destination', 'travel_date')
    
    
# admin.site.register()

