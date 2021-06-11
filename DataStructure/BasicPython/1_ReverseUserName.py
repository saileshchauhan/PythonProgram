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

def reverse_username_lastname(userFirstName,userLastName):
    '''
    Description:
        Method implements to reverse userfirstName and userLastName
    Parameters:
        userfirstName and userLastName as parameters.
    Returns:
        list of parameters after converting them to reverse.
    '''
    try:
        return [userFirstName[::-1],userLastName[::-1]]
    except Exception as ex:
        logging.critical(ex)

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
        regexName="^[a-zA-z]{3,}$"
        if(re.match(regexName,stringValue)):
            return stringValue
        logging.debug("Invalid Input")
        quit()
    except Exception as ex:
        logging.critical(ex)

returnList=reverse_username_lastname(userFirstName=validation(input("Enter your first Name\n")),userLastName=validation(input("Enter your last Name\n")))
logging.debug("User First Name in reverse {0} Last Name in reverse {1} ".format(returnList[0],returnList[1]))
