'''
@Author:Sailesh Chauhan
@Date:2021-06-10
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-10
@Title: Count string with two or more character and same character at first
        and last of the string.
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
    
def find_firstAndLast_same(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        newList=[]
        count=0
        for element in list:
            if(len(element)>2 and element[0]==element[len(element)-1]):
                count+=1
                newList.append(element)
        return count,newList
    except Exception as ex:
        logging.error(ex)

list=create_list()
returnList=find_firstAndLast_same(list)
print("The count is %s of elements with 2 or more character and same first and last character %s "%(returnList[0],returnList[1]))