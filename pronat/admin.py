from django.contrib import admin

from .models import *

admin.site.register(City)
admin.site.register(District)


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]