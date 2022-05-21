from import_export import resources
from .models import *

class DiagmosisResource(resources.ModelResource):
    class Meta:
        model = Diagmosis

class VisitResource(resources.ModelResource):
    class Meta:
        model = Visit

class MedicationResource(resources.ModelResource):
    class Meta:
        model = Medication


class problemsResource(resources.ModelResource):
    class Meta:
        model = problems

class SocialResource(resources.ModelResource):
    class Meta:
        model = Social

class LabResource(resources.ModelResource):
    class Meta:
        model = Lab


class MicroBiologyResource(resources.ModelResource):
    class Meta:
        model = MicroBiology

###########################
class N_DiagnosisResource(resources.ModelResource):
    class Meta:
        model = N_Diagnosis

class N_DrugResource(resources.ModelResource):
    class Meta:
        model = N_Drug

class N_LabResource(resources.ModelResource):
    class Meta:
        model = N_Lab

class N_ProblemResource(resources.ModelResource):
    class Meta:
        model = N_Problem

class N_ProcedureResource(resources.ModelResource):
    class Meta:
        model = N_Procedure

class N_VisitResource(resources.ModelResource):
    class Meta:
        model = N_Visit
