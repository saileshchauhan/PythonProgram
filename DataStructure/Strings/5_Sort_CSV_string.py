'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Print CSV String after sorting to CSV.
'''

#Importing logConfig for error logging
import logconfig
import logging,re

def create_string():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        userValue=validation(input("You can enter any word\n"))
        return userValue   
    except Exception as ex:
        logging.error(ex)

def validation(stringValue):
    '''
    Description:
        Provides validation for userinput.
    Parameters:
        stringValue it is userinput.
    Returns:
        correctString after validation.
    '''
    try:
        regexName="^[a-zA-Z0-9,.]{3,}[a-zA-Z]+$"
        if(re.match(regexName,stringValue)):
            return stringValue
        logging.debug("String Lenght must be more than 3")
    except Exception as ex:
        logging.critical(ex)

def csv_sorting(string):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        csvList=string.split(',')
        csvList.sort()
        logging.debug(list(set(csvList)))
    except Exception as ex:
        logging.critical(ex)

csvString=create_string()
csv_sorting(csvString)


