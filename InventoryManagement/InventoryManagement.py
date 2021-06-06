'''
@Author:Sailesh Chauhan
@Date:2021-06-05
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-05
@Title:Inventory Management 
'''
import json
import logging
from decouple import config 

FILE_PATH_LOG=config('log_File_Path')
FILE_PATH_JSON=config('json_File_Path')

logging.basicConfig(filename=FILE_PATH_LOG,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

class Inventory:
    '''
    Description:
        Name of class is Contact provides blue print to create custom object
        with attributes firstName,lastName,city,contact
    Function:
        No Function.
    Variables:
        Class Variables Name,Weight,PricePerKg.
    '''
    def __init__(self,name,weight,pricePerKg):
        self.name=name
        self.weight=weight
        self.pricePerKg=pricePerKg
        pass