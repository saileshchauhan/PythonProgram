'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title:Append user input to list and tuple then print.
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
        integer after validation.
    '''
    try:
        regexName="^[0-9]{1,}$"
        if(re.match(regexName,stringValue)):
            return int(stringValue)
        print("Invalid Input")
        quit()
    except Exception as ex:
        logging.critical(ex)

def input_to_list_tuple():
    '''
    Description:
        Prints values enterd by user in list and tuples.
    Parameters:
        None
    Returns:
        None.
    '''
    try:
        countOfEntry=validation(input("Enter count of list\n"))
        listNumber=[]
        tupleNumber=()
        for count in range(countOfEntry):
            userinput=validation(input("Enter whole number\n"))
            listNumber.append(str(userinput))
        tupleNumber=list(tupleNumber)
        tupleNumber=listNumber+tupleNumber
        tupleNumber=tuple(tupleNumber)
        print("Values in list ",listNumber)
        print("Values in Tuple",tupleNumber)
    except Exception as ex:
        logging.critical(ex)

input_to_list_tuple()