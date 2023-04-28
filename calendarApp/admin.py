from django.contrib import admin

from .models import Appointment, Business

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ["title","user","start_time"]

    search_fields = ["title"]

    list_filter = ["start_time"]

    class Meta:
        model = Appointment

admin.site.register(Business)