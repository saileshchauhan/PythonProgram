'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Array values using indexes.
'''

import logging,array
from decouple import config
#from DataStructure import logconfig
def print_array_using_index():
    '''
    Description:

    '''
    try:
        intArray=array.array('i',(5,5,3,4,2))
        for count in range(len(intArray)-1):
            print(intArray[count])
    except Exception as ex:
        logging.critical(ex)

print_array_using_index()