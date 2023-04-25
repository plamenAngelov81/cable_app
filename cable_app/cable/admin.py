from django.contrib import admin

from cable_app.cable.models import Cable, Order


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
