'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Lower case first n character of string.
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


def lowercase_first_n(string,n):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        firstPart=string[:n+1]
        secondPart=string[n:]
        return firstPart.lower()+secondPart
    except Exception as ex:
        logging.critical(ex)

string=create_string()
print(lowercase_first_n(string,3))