
# Register your models here.
from django.contrib import admin
from .models import EventCategory, Event


admin.site.register(EventCategory)
admin.site.register(Event)