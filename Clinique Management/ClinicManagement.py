'''
@Author:Sailesh Chauhan
@Date:2021-06-06
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-06
@Title:Clinic Management Application
'''

import json
import logging
from decouple import config

FILE_PATH_LOG=config('log_File_Path')
FILE_PATH_JSON=config('JSON_File_Path')

logging.basicConfig(filename=FILE_PATH_LOG,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

class Doctor:
    '''
    Description:
        Creates Custom object with properties name,id,specialization
        availability.
    Properties:
        Name,Id,Specialization,Availability
    '''
    def __init__(self,name,id,specialization,availability):
        self.Name=name
        self.Id=id
        self.Specialization=specialization
        self.Availability=int(availability)
        pass
class Patient:
    '''
    Description:
        Creates Custom object with properties name,id,mobileNumber,age.
    Properties:
        Name,Id,MobileNumber,Age.
    '''
    def __init__(self,name,id,mobileNumber,age):
        self.Name=name
        self.Id=id
        self.MobileNumber=mobileNumber
        self.Age=int(age)
        pass
recordDictionary={}

def load_JSON_file():
    '''
    Description:
        Method loads data from JSON using environment variable.
        To recordDictionary variable.
    Parameters:
        No Parameters.
    Return:
        None.
    '''
    try:
        global recordDictionary
        with open(FILE_PATH_JSON,'+r') as file:
            recordDictionary=json.load(file)
    except Exception as ex:
        logging.critical(ex)

def add_doctor_patient_entry(KEY):
    '''
    Description:
        Method add doctor and patient new entry to dictionary. Then
        to the JSON file. 
    Parameters:
        Takes one parameters as KEY to recordDictionary.
    Return:
        None.
    '''
    try:
        global recordDictionary
        if(KEY=='DOCTOR'):
            doctor=Doctor(input("Enter name of doctor\n"),input("Enter Id of doctor\n"),input("Enter Doctor Specialization\n"),input("Enter Doctor Availability\n"))
            doctorRecord={doctor.Id:doctor.__dict__}
            recordDictionary.setdefault(KEY,[]).append(doctorRecord)
        elif(KEY=='PATIENT'):
            patient=Patient(input("Enter name of patient\n"),input("Enter Id of patient\n"),input("Enter patient MobileNumber\n"),input("Enter patient Age\n"))
            patientRecord={patient.Id:patient.__dict__}
            recordDictionary.setdefault(KEY,[]).append(patientRecord)
    except Exception as ex:
        logging.critical(ex)

def write_to_JSON():
    '''
    Description:
        Method writes recordDictionary key value to JSON file.
        Using JSON module.
    Parameters:
        No Parameters.
    Return:
        None.
    '''
    try:
        with open(FILE_PATH_JSON,'+r') as file:
            file.write(json.dumps(recordDictionary,indent=4))
    except Exception as ex:
        logging.critical(ex)

def search_through_Dictionary(KEY,searchParameter,searchKeyword):
    '''
    Description:
        Method supplements search_entry method. It provides code reusability
        for search_entry method.
    Parameters:
        Takes 3 parameters KEY for accesing values. searchParameter contains 
        entry value to be searched. searchKeyword provides entry key to be
        searched.
    Return:
        None.
    '''
    try:
        listDoctors=recordDictionary.get(KEY,"Invalid Search")
        if(listDoctors=='Invalid Search'):
            print(listDoctors)
            quit
        for entry in listDoctors:
            for entryValue in entry.values():
                doctorName=entryValue.get(searchKeyword)
                if(doctorName==searchParameter):
                    print("Search complete {} with ID {} ".format(doctorName,entryValue.get("Id")))
    except Exception as ex:
        logging.critical(ex)

def search_entry(KEY):
    '''
    Description:
        Method uses search_through_Dictionary method. It provides feature for
        searching through DOCTOR and PATIENT records. This method provides 4 features.
    Parameters:
        Takes KEY as parameter to dictionary. To acess records.
    Return:
        None.
    '''
    try:
        if(KEY=='DOCTOR'):
            choice=''
            while(choice!='4'):
                print("1.Search By Name\n2.Search By Id\n3.Search By Specialization\n4.Stop Searching")
                choice=input("Make your search selection\n")
                if(choice=='1'):
                    searchParameter=input("Enter Name of doctor\n")
                    search_through_Dictionary(KEY,searchParameter,"Name")
                elif(choice=='2'):
                    searchParameter=input("Enter Id of doctor\n")
                    list=recordDictionary.get(KEY)
                    for entry in list:
                        for key,value in entry.items():
                            if(key==searchParameter):
                                id=value.get("Id")
                                print("Id of doctor {0}\nAll detail {1} ".format(id,value))
                elif(choice=='3'):
                    searchParameter=input("Enter Speciality\n")
                    search_through_Dictionary(KEY,searchParameter,"Specialization")
        elif(KEY=='PATIENT'):
            choice=''
            while(choice!='4'):
                print("1.Search By Name\n2.Search By Id\n3.Search By MobileNumber\n4.Stop Searching")
                choice=input("Make your search selection\n")
                if(choice=='1'):
                    searchParameter=input("Enter Name of Patient\n")
                    search_through_Dictionary(KEY,searchParameter,"Name")
                elif(choice=='2'):
                    searchParameter=input("Enter Id of doctor\n")
                    list=recordDictionary.get(KEY)
                    for entry in list:
                        for key,value in entry.items():
                            if(key==searchParameter):
                                id=value.get("Id")
                                print("Id of Patient {0}\nAll detail {1} ".format(id,value))
                elif(choice=='3'):
                    searchParameter=input("Enter MobileNumber\n")
                    search_through_Dictionary(KEY,searchParameter,"MobileNumber")
    except Exception as ex:
        logging.critical(ex)

