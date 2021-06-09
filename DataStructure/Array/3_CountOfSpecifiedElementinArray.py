'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Number of occurence of specified element in Array.
'''

import logging,re
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def user_input_to_array():
    '''
    Description:
    Parameters:
    Returns:
    '''
    array=[]
    choice=''
    print("Ener any number of values")
    while(choice.lower()!='q'):
        userValue=input("Enter value\n")
        array.append(userValue)
        print("Do you want to add more values \nPress C to continue\nQ to stop")
        choice=input("Enter choice")
    return array

def print_list(list):
    '''
    '''
    print(list)

print_list(list=user_input_to_array())

