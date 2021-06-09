'''
@Author:Sailesh Chauhan
@Date:2021-06-09
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Create, Clear, frozen Set function in Sets.
'''

#Importing logConfig for error logging
from typing import FrozenSet
import logconfig
import logging,re

def create_set():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultSet=set()
        choice=''
        print("You can enter any value in set")
        while(choice.lower()!='q'):
            userValue=validation(input("Enter value to add in set\n"))
            defaultSet.add(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return defaultSet
    except Exception as ex:
        logging.error(ex)

def find_max_min(set):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        return max(set),min(set)
    except Exception as ex:
        logging.error(ex)

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
            return int(stringValue)
        print("Invalid Input")
    except Exception as ex:
        logging.critical(ex)
try:
    set=create_set()
    returnlist=find_max_min(set)
    print("Maximum Values %s"%returnlist[0])
    print("Minimum Values %s"%returnlist[1])
except Exception as ex:
    logging.error(ex)