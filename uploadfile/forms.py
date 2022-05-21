from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


class DiagmosisData(forms.Form):
	class meta:
		model = Diagmosis
		fields = '__all__'

class VisitData(forms.Form):
	class meta:
		model = Visit
		fields = '__all__'

class MedicationData(forms.Form):
	class meta:
		model = Medication
		fields = '__all__'


class problemsData(forms.Form):
	class meta:
		model = problems
		fields = '__all__'

class SocialData(forms.Form):
	class meta:
		model = Social
		fields = '__all__'

class LabData(forms.Form):
	class meta:
		model = Lab
		fields = '__all__'


class MicroBiologyData(forms.Form):
	class meta:
		model = MicroBiology
		fields = '__all__'

class Disease_RegistryData(forms.Form):
	class meta:
		model = Disease_Registry
		fields = '__all__'
#################################################

class N_DiagnosisData(forms.Form):
	class meta:
		model = N_Diagnosis
		fields = '__all__'

class N_DrugData(forms.Form):
	class meta:
		model = N_Drug
		fields = '__all__'

class N_LabData(forms.Form):
	class meta:
		model = N_Lab
		fields = '__all__'

class N_ProblemData(forms.Form):
	class meta:
		model = N_Problem
		fields = '__all__'

class N_ProcedureData(forms.Form):
	class meta:
		model = N_Procedure
		fields = '__all__'

class VisitData(forms.Form):
	class meta:
		model = N_Visit
		fields = '__all__'



