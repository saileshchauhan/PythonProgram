'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title:Reverse user firstName and LastName.
'''

import logging,re
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def validation(stringValue):
    '''
    Description:
        Provides validation for userinput.
    Parameters:
        stringValue it is uerinput.
    Returns:
        correctString after validation.
    '''
    try:
        regexName="^[0-9]{1,}$"
        if(re.match(regexName,stringValue)):
            return stringValue
        print("Invalid Input")
        quit()
    except Exception as ex:
        logging.critical(ex)