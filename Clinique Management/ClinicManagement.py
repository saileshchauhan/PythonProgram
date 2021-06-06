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
