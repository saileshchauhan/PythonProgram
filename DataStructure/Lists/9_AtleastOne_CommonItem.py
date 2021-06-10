'''
@Author:Sailesh Chauhan
@Date:2021-06-10
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-10
@Title: Find out common item in both list.
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
        print("You can enter any value in list")
        while(choice.lower()!='q'):
            userValue=validation(input("Enter value to add in list\n"))
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

list1=create_list()
list2=create_list()

def atleast_one_common(list1,list2):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        for item in list1:
            for element in list2:
                if(item==element):
                    print(item)
                    return True
    except Exception as ex:
        logging.critical(ex)

atleast_one_common(list1,list2)
