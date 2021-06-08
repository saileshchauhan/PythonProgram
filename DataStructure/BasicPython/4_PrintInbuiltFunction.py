'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Definition of Inbuilt Function.
'''

import logging,re
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def print_definition(function):
    '''
    '''
    try:
        print(function.__doc__)
    except Exception as ex:
        logging.critical(ex)

print_definition(logging.getLoggerClass)