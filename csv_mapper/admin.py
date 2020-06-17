from django.contrib import admin

from .models import CSVMap


class CSVMapAdmin(admin.TabularInline):
    model = CSVMap
    fields = ['id_in_doc', 'first_name', 'last_name']


admin.site.register(CSVMap)
