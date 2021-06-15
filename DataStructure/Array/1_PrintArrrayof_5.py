'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Array values using indexes.
'''

import logging,array

import sys
sys.path.append(r"D:\OOPs\DataStructure")
import logconfig



def print_array_using_index(array):
    '''
    Description:
        Method prints array using indexes.
    Parameters:
        Method takes array of any size.
    Returns:
        Method logs array values to log file.
    '''
    try:
        
        for count in range(len(array)-1):
            logging.info(array[count])
    except Exception as ex:
        logging.critical(ex)

intArray=array.array('i',(5,5,3,4,2))
print_array_using_index(intArray)