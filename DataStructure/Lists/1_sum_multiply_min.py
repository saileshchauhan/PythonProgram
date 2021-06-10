'''
@Author:Sailesh Chauhan
@Date:2021-06-09
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Sum, Multiply and find min of elements in list.
'''

#Importing logConfig for error logging
from typing import FrozenSet
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
        regexName="^[0-9]{1,}$"
        if(re.match(regexName,stringValue)):
            return int(stringValue)
        print("Invalid Input")
    except Exception as ex:
        logging.critical(ex)

def find_sum_list(list,size):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        if(size==0):
            return 0
        return list[size-1]+find_sum_list(list,size-1)
    except Exception as ex:
        logging.error(ex)

def find_multiply_list(list,size):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        if(size==0):
            return 1
        return list[size-1]*find_multiply_list(list,size-1)
    except Exception as ex:
        logging.error(ex)

def find_min_list(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        value=list[0]
        for element in range(len(list)-1):
            if(value<element):
                value=element
        return value
    except Exception as ex:
        logging.error(ex)


try:
    list=create_list()
    totalSum=find_sum_list(list,len(list))
    totalMultiply=find_multiply_list(list,len(list))
    minValue=find_min_list(list)
    print("Total Sum of Values in list %s"%totalSum)
    print("Total Multiplication of Values in list %s"%totalMultiply)
    print("Minimum Value in list %s"%minValue)
except Exception as ex:
    logging.error(ex)