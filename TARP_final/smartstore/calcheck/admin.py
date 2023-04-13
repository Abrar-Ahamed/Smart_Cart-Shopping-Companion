from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import DiaryResource
# Register your models here.
from .models import Diary


class DiaryAdmin(ImportExportModelAdmin):
    resource_class = DiaryResource

admin.site.register(Diary, DiaryAdmin)