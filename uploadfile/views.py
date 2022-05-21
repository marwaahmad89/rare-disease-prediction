from django.shortcuts import render
from django.http import HttpResponse
from .resources import *
from .models import *
from tablib import Dataset

import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import time
import psycopg2

def export(request):
    person_resource = DiagmosisResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        Diagmosis_resource = DiagmosisResource()
        dataset = Dataset()
        new_var = request.FILES
        new_Diagmosis = new_var['myfile']

        imported_data = dataset.load(new_Diagmosis.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            #print(data[1])
            value = Diagmosis(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7], data[8],
                 data[9],
                 data[10],
                 data[11],
                 data[12],
                 data[13],
                 data[14],
                 data[15],
                 data[16],
                 data[17],
                 data[18],
                 data[19],
                 data[20],
                 data[21],
                 data[22],
                 data[23],
                 data[24],
                 data[25],
                 data[26],
                 data[27],
                 data[28],
                 data[29],
                 data[30]
                 )
            value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'input.html')

def Import_csv(request):
    print('s')
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        
        #1- Assume that the user uploaded an excel file
        start_time_upload = time.time()
        dia_exceldata = pd.read_excel("."+excel_file,sheet_name='Diagmosis')
        Vis_exceldata = pd.read_excel("."+excel_file,sheet_name='Visits')       
        Med_exceldata= pd.read_excel("."+excel_file,sheet_name='Medication')
        pro_exceldata= pd.read_excel("."+excel_file,sheet_name='problems')
        Soc_exceldata=pd.read_excel("."+excel_file,sheet_name='Social')
        Lab_exceldata=pd.read_excel("."+excel_file,sheet_name='Lab')
        Mic_exceldata=pd.read_excel("."+excel_file,sheet_name='MicroBiology')
        
        print("file  uploaded succesfully it takes {} seconds".format(time.time() - start_time_upload))
#Variable  ###########################################
        Cardiomyopathy_list=['I42.5','425.4','I42.1','I42.2','I42.0','425.3','I42.9']
        lack_development_list=['R62.50']
        hypotonia_list=['728.9','P94.2']
        feeding_difficulties_list=['783.3','R63.3']
        respiratory_infection_list=['J22']
        ck_value=300
        ck_order='Creatine Kinase'
        print('Variables set succesfully')

#Cardiomyopathy####################################    
        df_filter1=dia_exceldata.loc[dia_exceldata['Diagnosis Description'].isin(Cardiomyopathy_list)]
        df_filter2=pro_exceldata.loc[pro_exceldata['Problem Code'].isin(Cardiomyopathy_list)]
        Cardiomyopathy_p=pd.concat([df_filter1['PERSON_ID'],df_filter2['PERSON_ID']]).to_frame().dropna().drop_duplicates('PERSON_ID')
        for i in Cardiomyopathy_p.itertuples():
            obj = Disease_Registry.objects.update_or_create(person_id=i.PERSON_ID,cardiomyopathy=True)
        print('Cardiomyopathy rule detected succesfully')

#hypotonia ##################################
        df_filter=dia_exceldata.loc[dia_exceldata['Diagnosis Description'].isin(hypotonia_list)].drop_duplicates('PERSON_ID')
        hypotonia_p=(df_filter['PERSON_ID'].dropna()).to_frame()
        hypotonia_p.insert(1, 'hypotonia', 'True')
        for i in hypotonia_p.itertuples():
            obj = Disease_Registry.objects.update_or_create(person_id=i.PERSON_ID ,defaults={'hypotonia': i.hypotonia})
        
        print('hypotonia rule detected succesfully')
            
#Feeding_difficulties ##############################
        df_filter=dia_exceldata.loc[dia_exceldata['Diagnosis Description'].isin(feeding_difficulties_list)].drop_duplicates('PERSON_ID')
        Feeding_diffi_P=(df_filter['PERSON_ID'].dropna()).to_frame()
        Feeding_diffi_P.insert(1, 'Feeding_difficulties', 'True')
        for i in Feeding_diffi_P.itertuples():
            obj = Disease_Registry.objects.update_or_create(person_id=i.PERSON_ID ,defaults={'feeding_difficulty': i.Feeding_difficulties})

        print('Feeding_difficulties rule detected succesfully')

#chest infection###################################
        df_filter=dia_exceldata.loc[dia_exceldata['Diagnosis Description'].isin(respiratory_infection_list)].drop_duplicates('PERSON_ID')
        chest_infec_P=(df_filter['PERSON_ID'].dropna()).to_frame()
        chest_infec_P.insert(1, 'chest_infection', 'True')
        for i in chest_infec_P.itertuples():
            obj = Disease_Registry.objects.update_or_create(person_id=i.PERSON_ID ,defaults={'respiratory_infection': i.chest_infection})       
        
        print('chest infection rule detected succesfully')

#creatine kinase###################################
        df_filter=Lab_exceldata.where((Lab_exceldata['Order Mnemonic']==ck_order)&(Lab_exceldata['Result Value Numeric']>ck_value)).drop_duplicates('PERSON_ID')
        CK_P=(df_filter['PERSON_ID'].dropna()).to_frame()
        CK_P.insert(1, 'Creatine_Kinase', 'True')
        for i in CK_P.itertuples():
            obj = Disease_Registry.objects.update_or_create(person_id=i.PERSON_ID ,defaults={'p_ck': i.Creatine_Kinase})       
                 
        print('creatine kinase rule detected succesfully')

#lack_development##########################################
        df_filter=dia_exceldata.loc[dia_exceldata['Diagnosis Description'].isin(lack_development_list)].drop_duplicates('PERSON_ID')
        lack_development_p=(df_filter['PERSON_ID'].dropna()).to_frame()
        lack_development_p.insert(1, 'lack_development', 'True')
        for i in lack_development_p.itertuples():
            obj = Disease_Registry.objects.update_or_create(person_id=i.PERSON_ID,defaults={'physiological_development': i.lack_development})        
        print('lack_development rule detected succesfully')

#POMPE FLAG #################################################
#2- push the data to DB##################################
        
        start_time_upload = time.time()
        #******Visit***********
        Visit_frame = Vis_exceldata
        Visit_frame.columns=['ID','ENCNTR_ID','PERSON_ID','Financial_Number','MRN','CMRN','Emirates_id','Facility','Building','Nursing_Unit','Current_Age',
                             'Medical_Service','Encounter_Type','Sex','Nationality','Birth_Date','Registration_Date','Discharge_Date','Discharge_Disposition',
                             'Deceased_Date','Height','Weight']
        Visit_frame=Visit_frame.replace({pd.NaT: None})
        for i in Visit_frame.itertuples():
            #process per table
            obj = Visit.objects.update_or_create(ID=i.ID,ENCNTR_ID=i.ENCNTR_ID,PERSON_ID=i.PERSON_ID,Financial_Number=i.Financial_Number,MRN=i.MRN,CMRN=i.CMRN,
                                                 Emirates_id=i.Emirates_id,Facility=i.Facility,Building=i.Building,Nursing_Unit=i.Nursing_Unit,Current_Age=i.Current_Age,
                                                 Medical_Service=i.Medical_Service,Encounter_Type=i.Encounter_Type,Sex=i.Sex,Nationality=i.Nationality,Birth_Date=i.Birth_Date,
                                                 Registration_Date=i.Registration_Date,Discharge_Date=i.Discharge_Date,Discharge_Disposition=i.Discharge_Disposition,
                                                 Deceased_Date=i.Deceased_Date,Height=i.Height,Weight=i.Weight)

            print(type(obj))


        #*********Diagnosis*******
        Diagmosis_frame = dia_exceldata
        Diagmosis_frame.columns=['ID', 'ENCNTR_ID', 'PERSON_ID','Financial_Number','MRN','CMRN', 'Emirates_id','Facility', 'Building', 'Nursing_Unit', 'Age_at_diagnosis', 
                         'Current_Age', 'Medical_Service', 'Encounter_Type', 'Sex','Nationality','Birth_Date','Registration_Date','Discharge_Date','Discharge_Disposition','Deceased_Date',
                         'Diagnosis_Description','Diagnosis_Code','Diagnosis_Date','Diagnosis_Code_Source','List_Number','Diagnosis_Ranking', 'Diagnosed_personnel','Diagnosis_Display','Diagnosis_Confirmation','Diagnosis_Type']
        Diagmosis_frame=Diagmosis_frame.replace({pd.NaT: None})
        #print(Diagmosis_frame.columns)
        for Diagmosis_frame in Diagmosis_frame.itertuples():
            #process per table
            obj = Diagmosis.objects.update_or_create(ID=Diagmosis_frame.ID,ENCNTR_ID=Diagmosis_frame.ENCNTR_ID,PERSON_ID=Diagmosis_frame.PERSON_ID,Financial_Number=Diagmosis_frame.Financial_Number,
                                           MRN=Diagmosis_frame.MRN,CMRN=Diagmosis_frame.CMRN,Emirates_id=Diagmosis_frame.Emirates_id,Facility=Diagmosis_frame.Facility,Building=Diagmosis_frame.Building,
                                           Nursing_Unit=Diagmosis_frame.Nursing_Unit,Age_at_diagnosis=Diagmosis_frame.Age_at_diagnosis,Current_Age=Diagmosis_frame.Current_Age,
                                           Medical_Service=Diagmosis_frame.Medical_Service,Encounter_Type=Diagmosis_frame.Encounter_Type,Sex=Diagmosis_frame.Sex,Nationality=Diagmosis_frame.Nationality,
                                           Birth_Date=Diagmosis_frame.Birth_Date,Registration_Date=Diagmosis_frame.Registration_Date,Discharge_Date=Diagmosis_frame.Discharge_Date,Discharge_Disposition=Diagmosis_frame.Discharge_Disposition,
                                           Deceased_Date=Diagmosis_frame.Deceased_Date,Diagnosis_Description=Diagmosis_frame.Diagnosis_Description,Diagnosis_Code=Diagmosis_frame.Diagnosis_Code,Diagnosis_Date=Diagmosis_frame.Diagnosis_Date,
                                           Diagnosis_Code_Source=Diagmosis_frame.Diagnosis_Code_Source,List_Number=Diagmosis_frame.List_Number,Diagnosis_Ranking=Diagmosis_frame.Diagnosis_Ranking,Diagnosed_personnel=Diagmosis_frame.Diagnosed_personnel,
                                           Diagnosis_Display=Diagmosis_frame.Diagnosis_Display,Diagnosis_Confirmation=Diagmosis_frame.Diagnosis_Confirmation,Diagnosis_Type=Diagmosis_frame.Diagnosis_Type)
            print(type(obj))


        #Medication
        Medication_frame = Med_exceldata
        Medication_frame.columns=['ID','PERSON_ID','ORDER_ID','ENCNTR_ID','Order_Name','Completed_Date','Order_Date','Diagnosis','Diagnosis_Code','Order_Code']
        Medication_frame=Medication_frame.replace({pd.NaT: None})
        for i in Medication_frame.itertuples():
            #process per table
            obj = Medication.objects.update_or_create(ID=i.ID,PERSON_ID=i.PERSON_ID,ORDER_ID=i.ORDER_ID,ENCNTR_ID=i.ENCNTR_ID,Order_Name=i.Order_Name,Completed_Date=i.Completed_Date,
                                                      Order_Date=i.Order_Date,Diagnosis=i.Diagnosis,Diagnosis_Code=i.Diagnosis_Code,Order_Code=i.Order_Code)
            print(type(obj))


        #problems
        problems_frame = pro_exceldata
        problems_frame.columns=['ID','PERSON_ID','Number','Problem_Start_Date','Problem_End_Date','Problem_ID','Problem_Display','Problem_Code','Problem_Description',
                                'Problem_Source'] 
        problems_frame=problems_frame.replace({pd.NaT: None})
        for i in problems_frame.itertuples():
            #process per table
            obj = problems.objects.update_or_create(ID=i.ID,PERSON_ID=i.PERSON_ID,Number=i.Number,Problem_Start_Date=i.Problem_Start_Date,Problem_End_Date=i.Problem_End_Date,
                                                    Problem_ID=i.Problem_ID,Problem_Display=i.Problem_Display,Problem_Code=i.Problem_Code,Problem_Description=i.Problem_Description,
                                                    Problem_Source=i.Problem_Source)

            print(type(obj))

        #Social
        Social_frame = Soc_exceldata
        Social_frame.columns=['ID','PERSON_ID','ENCNTR_ID','Social_History','Social_History_Description','Performed_date'] 
        Social_frame=Social_frame.replace({pd.NaT: None})

        for i in Social_frame.itertuples():
            #process per table
            obj = Social.objects.update_or_create(ID=i.ID,PERSON_ID=i.PERSON_ID,ENCNTR_ID=i.ENCNTR_ID,Social_History=i.Social_History,Social_History_Description=i.Social_History_Description,
                                                  Performed_date=i.Performed_date)
            print(type(obj))


        #lab
        Lab_frame = Lab_exceldata
        Lab_frame.columns=['ID','PERSON_ID','ORDER_ID','ENCNTR_ID','Order_Name','Order_Mnemonic','Order_Description','Order_Category','Order_Sub_Category',
                           'Completed_Date','Order_Date','Task_Assay','Result_Status','Result_Value_Alpha','Result_Value_Numeric','Result_Value','Unit',
                           'Result_Text','Order_Code'] 
        Lab_frame=Lab_frame.replace({pd.NaT: None})
        for i in Lab_frame.itertuples():
            #process per table
            obj = Lab.objects.update_or_create(ID=i.ID,PERSON_ID=i.PERSON_ID,ORDER_ID=i.ORDER_ID,ENCNTR_ID=i.ENCNTR_ID,Order_Name=i.Order_Name,Order_Mnemonic=i.Order_Mnemonic,
                                               Order_Description=i.Order_Description,Order_Category=i.Order_Category,Order_Sub_Category=i.Order_Sub_Category,
                                               Completed_Date=i.Completed_Date,Order_Date=i.Order_Date,Task_Assay=i.Task_Assay,Result_Status=i.Result_Status,
                                               Result_Value_Alpha=i.Result_Value_Alpha,Result_Value_Numeric=i.Result_Value_Numeric,Result_Value=i.Result_Value,Unit=i.Unit,
                                               Result_Text=i.Result_Text,Order_Code=i.Order_Code)
            print(type(obj))
        
        #MicroBiology
        MicroBiology_frame = Mic_exceldata
        MicroBiology_frame.columns=['ID','PERSON_ID','ORDER_ID','ENCNTR_ID','Order_Name','Order_Mnemonic','Order_Description','Order_Category','Order_Sub_Category',
                                    'Completed_Date','Order_Date','Response_Display','Response_Text','Catalog_Type','Order_Code'] 
        MicroBiology_frame=MicroBiology_frame.replace({pd.NaT: None})
        for i in MicroBiology_frame.itertuples():
            #process per table
            obj = MicroBiology.objects.update_or_create(ID=i.ID,PERSON_ID=i.PERSON_ID,ORDER_ID=i.ORDER_ID,ENCNTR_ID=i.ENCNTR_ID,Order_Name=i.Order_Name,
                                                        Order_Mnemonic=i.Order_Mnemonic,Order_Description=i.Order_Description,Order_Category=i.Order_Category,
                                                        Order_Sub_Category=i.Order_Sub_Category,Completed_Date=i.Completed_Date,Order_Date=i.Order_Date,
                                                        Response_Display=i.Response_Display,Response_Text=i.Response_Text,Catalog_Type=i.Catalog_Type,Order_Code=i.Order_Code
                                                        )
            print(type(obj))
        print("file  pushed succesfully it takes {} seconds".format(time.time() - start_time_upload))

        start_time_AI = time.time()
    
    
    return render(request, 'importexcel.html')
