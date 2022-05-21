from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms 
from datetime import datetime

class Diagmosis(models.Model):
    ID = models.BigIntegerField(unique=True)
    ENCNTR_ID = models.BigIntegerField(null=True, blank=True)
    PERSON_ID= models.BigIntegerField(null=True, blank=True)
    Financial_Number=models.TextField(null=True, blank=True)
    MRN=models.TextField(null=True, blank=True)
    CMRN=models.TextField(null=True, blank=True)
    Emirates_id=models.TextField(null=True, blank=True)
    Facility=models.TextField(null=True, blank=True)
    Building=models.TextField(null=True, blank=True)
    Nursing_Unit=models.TextField(null=True, blank=True)
    Age_at_diagnosis=models.FloatField(null=True, blank=True)
    Current_Age=models.BigIntegerField(null=True, blank=True)
    Medical_Service=models.TextField(null=True, blank=True)
    Encounter_Type=models.TextField(null=True, blank=True)
    Sex=models.TextField(null=True, blank=True)
    Nationality=models.TextField(null=True, blank=True)
    Birth_Date=models.DateTimeField(null=True, blank=True)
    Registration_Date=models.DateTimeField(null=True, blank=True)
    Discharge_Date=models.DateTimeField(null=True, blank=True)
    Discharge_Disposition=models.TextField(null=True, blank=True)
    Deceased_Date=models.DateTimeField(null=True, blank=True)
    Diagnosis_Description=models.TextField(null=True, blank=True)
    Diagnosis_Code=models.TextField(null=True, blank=True)
    Diagnosis_Date=models.DateTimeField(null=True, blank=True)
    Diagnosis_Code_Source=models.TextField(null=True, blank=True)
    List_Number=models.BigIntegerField(null=True, blank=True)
    Diagnosis_Ranking=models.TextField(null=True, blank=True)
    Diagnosed_personnel=models.TextField(null=True, blank=True)
    Diagnosis_Display=models.TextField(null=True, blank=True)
    Diagnosis_Confirmation=models.TextField(null=True, blank=True)
    Diagnosis_Type=models.TextField(null=True, blank=True)

    class Meta:
     db_table = "Diagmosis" 
     verbose_name_plural="old_Diagmosis" 
    
    def __int__(self):
        return self.ENCNTR_ID



class Visit(models.Model):
     ID=models.BigIntegerField(unique=True)
     ENCNTR_ID = models.BigIntegerField(null=True, blank=True)
     PERSON_ID= models.BigIntegerField(null=True, blank=True)
     Financial_Number=models.TextField(null=True, blank=True)
     MRN=models.TextField(null=True, blank=True)
     CMRN=models.TextField(null=True, blank=True)
     Emirates_id=models.TextField(null=True, blank=True)
     Facility=models.TextField(null=True, blank=True)
     Building=models.TextField(null=True, blank=True)
     Nursing_Unit=models.TextField(null=True, blank=True)
     Current_Age=models.BigIntegerField(null=True, blank=True)
     Medical_Service=models.TextField(null=True, blank=True)
     Encounter_Type=models.TextField(null=True, blank=True)
     Sex=models.TextField(null=True, blank=True)
     Nationality=models.TextField(null=True, blank=True)
     Birth_Date=models.DateTimeField(null=True, blank=True)
     Registration_Date=models.DateTimeField(null=True, blank=True)
     Discharge_Date=models.DateTimeField(null=True, blank=True)
     Discharge_Disposition=models.TextField(null=True, blank=True)
     Deceased_Date=models.DateTimeField(null=True, blank=True)
     Height=models.FloatField(null=True, blank=True)
     Weight=models.FloatField(null=True, blank=True)
     
     class Meta:
       db_table = "Visit" 
       verbose_name_plural="old_Visit" 

     def __int__(self):
        return self.ENCNTR_ID


class Medication(models.Model):
     ID=models.BigIntegerField(unique=True)
     PERSON_ID= models.BigIntegerField(null=True, blank=True)
     ORDER_ID=models.BigIntegerField(null=True, blank=True)
     ENCNTR_ID = models.BigIntegerField(null=True, blank=True)
     Order_Name=models.TextField(null=True, blank=True)
     Completed_Date=models.DateTimeField(null=True, blank=True)
     Order_Date=models.DateTimeField(null=True, blank=True)
     Diagnosis=models.TextField(null=True, blank=True)
     Diagnosis_Code=models.TextField(null=True, blank=True)
     Order_Code=models.BigIntegerField(null=True, blank=True)

     class Meta:
       db_table = "Medication" 
       verbose_name_plural="old_Medication" 

     def __int__(self):
        return self.ORDER_ID    
    

class problems(models.Model):
     ID=models.BigIntegerField(unique=True)
     PERSON_ID= models.BigIntegerField(null=True, blank=True)
     Number=models.BigIntegerField(null=True, blank=True)
     Problem_Start_Date=models.DateTimeField(null=True, blank=True)
     Problem_End_Date=models.DateTimeField(null=True, blank=True)
     Problem_ID=models.BigIntegerField(null=True, blank=True)
     Problem_Display=models.TextField(null=True, blank=True)
     Problem_Code=models.TextField(null=True, blank=True)
     Problem_Description=models.TextField(null=True, blank=True)
     Problem_Source=models.TextField(null=True, blank=True)


     class Meta:
       db_table = "Problem" 
       verbose_name_plural="old_Problem" 

     def __int__(self):
        return self.Number   


class Social(models.Model):
     ID=models.BigIntegerField()
     PERSON_ID= models.BigIntegerField(null=True, blank=True)
     ENCNTR_ID=models.BigIntegerField(null=True, blank=True)
     Social_History=models.TextField(null=True, blank=True)
     Social_History_Description=models.TextField(null=True, blank=True)
     Performed_date=models.DateTimeField(null=True, blank=True)
     
     class Meta:
       db_table = "Social" 
       verbose_name_plural="old_Social" 

     def __str__(self):
        return self.Social_History  



class Lab(models.Model):
     ID=models.BigIntegerField(unique=True)
     PERSON_ID= models.BigIntegerField(null=True, blank=True)
     ORDER_ID=models.BigIntegerField(null=True, blank=True)
     ENCNTR_ID = models.BigIntegerField(null=True, blank=True)
     Order_Name=models.TextField(null=True, blank=True)
     Order_Mnemonic=models.TextField(null=True, blank=True)
     Order_Description=models.TextField(null=True, blank=True)
     Order_Category=models.TextField(null=True, blank=True)
     Order_Sub_Category=models.TextField(null=True, blank=True)
     Completed_Date=models.DateTimeField(null=True, blank=True)
     Order_Date=models.DateTimeField(null=True, blank=True)
     Task_Assay=models.TextField(null=True, blank=True)
     Result_Status=models.TextField(null=True, blank=True)
     Result_Value_Alpha=models.TextField(null=True, blank=True)
     Result_Value_Numeric=models.FloatField(null=True, blank=True)
     Result_Value=models.DateTimeField(null=True, blank=True)
     Unit=models.TextField(null=True, blank=True)
     Result_Text=models.TextField(null=True, blank=True)
     Order_Code= models.BigIntegerField(null=True, blank=True)
     
     class Meta:
       db_table = "Lab"
       verbose_name_plural="old_Lab" 

     def __int__(self):
        return self.ORDER_ID  

class MicroBiology(models.Model):
     ID=models.BigIntegerField(unique=True)
     PERSON_ID= models.BigIntegerField(null=True, blank=True)
     ORDER_ID=models.BigIntegerField(null=True, blank=True)
     ENCNTR_ID = models.BigIntegerField(null=True, blank=True)
     Order_Name=models.TextField(null=True, blank=True)
     Order_Mnemonic=models.TextField(null=True, blank=True)
     Order_Description=models.TextField(null=True, blank=True)
     Order_Category=models.TextField(null=True, blank=True)
     Order_Sub_Category=models.TextField(null=True, blank=True)
     Completed_Date=models.DateTimeField(null=True, blank=True)
     Order_Date=models.DateTimeField(null=True, blank=True)
     Response_Display=models.TextField(null=True, blank=True)
     Response_Text=models.TextField(null=True, blank=True)
     Catalog_Type=models.TextField(null=True, blank=True)
     Order_Code=models.FloatField(null=True, blank=True)

     class Meta:
       db_table = "Microbiology"
       verbose_name_plural="old_Microbiology" 

     def __int__(self):
        return self.ORDER_ID 
      



class Disease_Registry(models.Model):
     person_id=models.BigIntegerField(unique=True)
     cardiomyopathy=models.BooleanField(default=False)
     hypotonia=models.BooleanField(default=False)
     physiological_development=models.BooleanField(default=False)
     p_ck=models.BooleanField(default=False)
     feeding_difficulty=models.BooleanField(default=False)
     respiratory_infection=models.BooleanField(default=False)
     pompe_patient=models.BooleanField(default=False)
     con_pompe_patient=models.BooleanField(null=True, blank=True)
     
     class Meta:
       db_table = "Disease Registry"
       verbose_name_plural="old_Disease Registry"
     def __int__(self):
        return self.person_id 


###############################################
class N_Diagnosis(models.Model):
    PERSONID= models.BigIntegerField(null=True, blank=True)
    ENCNTRID = models.BigIntegerField(null=True, blank=True)
    DIAGNOSISID = models.BigIntegerField(null=True, blank=True)
    ONSETDATE=models.DateTimeField(null=True, blank=True)
    DIAGNOSIS=models.TextField(null=True, blank=True)
    DESCRIPTION=models.TextField(null=True, blank=True)
    CLASSIFICATION=models.TextField(null=True, blank=True)
    CLASS=models.TextField(null=True, blank=True)
    TYPE=models.TextField(null=True, blank=True)
   
    
    class Meta:
     db_table = "N_Diagnosis" 
     verbose_name_plural="Diagnosis" 
    

    def __int__(self):
        return self.Encntr_ID

class N_Visit(models.Model):
     PERSONID=models.BigIntegerField(null=True, blank=True)
     ENCNTRID = models.BigIntegerField(null=True, blank=True)
     EPI=models.TextField(null=True, blank=True)
     MRN=models.TextField(null=True, blank=True)
     CLINICALEVENTID=models.BigIntegerField(null=True, blank=True)
     EVENTDATETIME=models.DateTimeField(null=True, blank=True)
     EVENTNAME=models.TextField(null=True, blank=True)
     EVENTRESULT=models.TextField(null=True, blank=True)
     RESULTUNIT=models.TextField(null=True, blank=True)
     
     class Meta:
       db_table = "N_Visit" 
       verbose_name_plural="Visit" 

     def __int__(self):
        return self.ENCNTRID

class N_Drug(models.Model):
     PERSONID=models.BigIntegerField(null=True, blank=True)
     ENCNTRID = models.BigIntegerField(null=True, blank=True)
     ORDERID = models.BigIntegerField(null=True, blank=True)
     ORDERMNEMONIC=models.TextField(null=True, blank=True)
     ORDERDETAIL=models.TextField(null=True, blank=True)
     ORDERDATE=models.DateTimeField(null=True, blank=True)



     class Meta:
       db_table = "N_Drug" 
       verbose_name_plural="Drug" 

     def __int__(self):
        return self.ORDERID   

class N_Lab(models.Model):
     PERSONID=models.BigIntegerField(null=True, blank=True)
     ENCNTRID = models.BigIntegerField(null=True, blank=True)
     ORDERID = models.BigIntegerField(null=True, blank=True)
     ORDERMNEMONIC=models.TextField(null=True, blank=True)
     ORDERDATE=models.DateTimeField(null=True, blank=True)
     RESULTID=models.BigIntegerField(null=True, blank=True)
     RESULTVALUE=models.TextField(null=True, blank=True)

     class Meta:
       db_table = "N_Lab" 
       verbose_name_plural="Lab" 

     def __int__(self):
        return self.ORDERID    

class N_Problem(models.Model):
     PERSONID=models.BigIntegerField(null=True, blank=True)
     PROBLEMID = models.BigIntegerField(null=True, blank=True)
     ONSETDATE=models.DateTimeField(null=True, blank=True)
     PROBLEM=models.TextField(null=True, blank=True)
     DESCRIPTION=models.TextField(null=True, blank=True)
  


     class Meta:
       db_table = "N_Problem" 
       verbose_name_plural="Problem" 

     def __int__(self):
        return self.PROBLEMID


class N_Procedure(models.Model):
     #Person_ID=models.BigIntegerField(null=True, blank=True)
     ENCNTRID = models.BigIntegerField(null=True, blank=True)
     PROCEDUREID = models.BigIntegerField(null=True, blank=True)
     PROCEDUREDATE=models.DateTimeField(null=True, blank=True)
     PPROCEDURE=models.TextField(null=True, blank=True)
     DESCRIPTION=models.TextField(null=True, blank=True)

     class Meta:
       db_table = "N_Procedure" 
       verbose_name_plural="Procedure" 

     def __int__(self):
        return self.PROCEDUREID 


