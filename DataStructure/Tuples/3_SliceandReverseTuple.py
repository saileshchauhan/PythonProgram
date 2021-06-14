'''
@Author:Sailesh Chauhan
@Date:2021-06-12
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-12
@Title: Slice and Reverse The Tuple.
'''

#Importing logConfig for error logging
from typing import DefaultDict
from Tuples import logconfig
import logging

def create_tuple():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultList=list()
        choice=''
        print("You can enter any value in set")
        while(choice.lower()!='q'):
            userValue=input("Enter value to add in set\n")
            defaultList.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return tuple(defaultList)
    except Exception as ex:
        logging.error(ex)

def reverese(tupleParameter):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultlist=list(tupleParameter)
        reverseList=defaultlist[::-1]
        return tuple(reverseList)
    except Exception as ex:
        logging.critical(ex)

def slice_tuple(tupleParameter,n):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultlist=list(tupleParameter)
        sliceList=defaultlist[n:n+2]
        return tuple(sliceList)
    except Exception as ex:
        logging.critical(ex)

newTuple=create_tuple()
print("Tuple after reversing %s"%reverese(newTuple))
print("Tuple after slicing first two elements %s"%slice_tuple(newTuple,0))