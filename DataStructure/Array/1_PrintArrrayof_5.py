'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Array values using indexes.
'''

import logging
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def print_array_using_index():
    '''
    '''
    try:
        array=list(input("Enter 5 number without space then enter "))
        for count in range(len(array)):
            print(array[count])
    except Exception as ex:
        logging.critical(ex)

print_array_using_index()