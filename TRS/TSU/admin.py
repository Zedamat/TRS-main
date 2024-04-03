from django.contrib import admin

# Register your models here.
from . models import Record
from . models import Product
from . models import Nation
from . models import Sex
from . models import Purpose

from import_export.admin import ImportExportModelAdmin



admin.site.register(Record, ImportExportModelAdmin)
admin.site.register(Product)
admin.site.register(Nation)
admin.site.register(Sex)
admin.site.register(Purpose)
