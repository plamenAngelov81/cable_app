from django.contrib import admin

from cable_app.cable.models import Cable


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    pass
