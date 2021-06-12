'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Print Input from user in uppercase and lower.
'''

#Importing logConfig for error logging

import logconfig
import logging,re

def create_word():
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

def lowercase_uppercase(word):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        logging.debug("User Input in Upper Case %s",word.upper())
        logging.debug("User Input in Upper Case %s",word.lower())
    except Exception as ex:
        logging.critical(ex) 

word=create_word()
lowercase_uppercase(word)