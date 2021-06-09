'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Create set
'''

#Importing logConfig for error logging
import logconfig
import logging

def create_set():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultSet=set()
        choice=''
        print("Ener any number of values to enter in array")
        while(choice.lower()!='q'):
            userValue=input("Enter value\n")
            defaultSet.add(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return defaultSet
    except Exception as ex:
        logging.error(ex)


def iterate_set(set=create_set()):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        for eachSetItem in set:
            print(eachSetItem)
    except Exception as ex:
        logging.error(ex)

iterate_set()
