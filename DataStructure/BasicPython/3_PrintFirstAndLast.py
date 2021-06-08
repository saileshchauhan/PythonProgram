'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title:Print first and Last Index of List.
'''

import logging,re
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def print_list_index(list):
    '''
    Description:
        Print values at given index in list.
    Parameters:
        Takes list as parameter.
    Return:
        None.
    '''
    try:
        print(list[0])
        print(list[len(list)-1])
    except Exception as ex:
        logging.critical(ex)

print_list_index(["Red","Green","White","Black"])