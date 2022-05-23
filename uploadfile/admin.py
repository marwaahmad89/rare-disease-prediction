import resource
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib import admin
from django.contrib import admin
# Need to import this since auth models get registered on import.
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from .resources import N_VisitResource

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)





######################
@admin.register(N_Diagnosis)
class N_DiagnosisAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in N_Diagnosis._meta.get_fields()]

@admin.register(N_Drug)
class N_DrugAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in N_Drug._meta.get_fields()]


@admin.register(N_Lab)
class N_LabAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in N_Lab._meta.get_fields()]

@admin.register(N_Problem)
class N_ProblemAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in N_Problem._meta.get_fields()]

@admin.register(N_Procedure)
class N_ProcedureAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in N_Procedure._meta.get_fields()]

@admin.register(N_Visit)
class N_VisitAdmin(ImportExportModelAdmin):
    resource_class = N_VisitResource
    list_display = [field.name for field in N_Visit._meta.get_fields()]

