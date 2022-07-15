from django.contrib import admin
from auto.models import Auto


class AutoAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer', 'model', 'color', 'plate_number',
         'production_year', 'vin', 'certificate_id',
        )

admin.site.register(Auto, AutoAdmin)