from django.contrib import admin

# Register your models here.
from . models import Data
from import_export.admin import ImportExportActionModelAdmin
admin.site.register(Data, ImportExportActionModelAdmin)