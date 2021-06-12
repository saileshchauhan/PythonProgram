'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Create set Add Element Iterate through set element.
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
        print("You can enter any value in set")
        while(choice.lower()!='q'):
            userValue=input("Enter value to add in set\n")
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
