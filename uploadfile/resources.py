from import_export import resources
from dateutil import parser
from datetime import datetime
from .models import *
import pytz



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

    def get_instance(self, instance_loader, row):
        # convert date time to django format
        row['EVENTDATETIME'] = parser.parse(row['EVENTDATETIME']).replace(tzinfo=pytz.UTC)
        # convert to integere
        row['PERSONID'] = int(row['PERSONID'])

    class Meta:
        model = N_Visit
