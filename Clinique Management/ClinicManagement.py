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
