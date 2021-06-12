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
try:
    set=create_set()
    print(set)
    print("Frozen Set ",frozenset(set))
    print("Set after clearing ",set.clear())
except Exception as ex:
    logging.critical(ex)