'''
@Author:Sailesh Chauhan
@Date:2021-06-09
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-10
@Title: Sum, Multiply and find min of elements in list.
'''

#Importing logConfig for error logging

import logconfig
import logging,re

def create_list():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultList=[]
        choice=''
        print("You can enter any value in set")
        while(choice.lower()!='q'):
            userValue=validation(input("Enter value to add in set\n"))
            defaultList.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return defaultList
    except Exception as ex:
        logging.error(ex)

def validation(stringValue):
    '''
    Description:
        Provides validation for userinput.
    Parameters:
        stringValue it is userinput.
    Returns:
        correctString after converting it to int validation.
    '''
    try:
        regexName="^[0-9a-zA-Z]{1,}$"
        if(re.match(regexName,stringValue)):
            return (stringValue)
        print("Invalid Input")
    except Exception as ex:
        logging.critical(ex)