'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Remove first occurence of specified element in Array.
'''

import logging,re
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(process)d - %(asctime)s - %(levelname)s - %(message)s')

def user_input_to_array():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        raise ValueError("Exception as occured")
        array=[]
        choice=''
        print("Ener any number of values to enter in array")
        while(choice.lower()!='q'):
            userValue=input("Enter value\n")
            array.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return array
    except Exception as ex:
        logging.critical(ex)

def remove_first_occurence_specific_element_array(list,userSelection):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        count=0
        for index in range(len(list)-1):
            if(list[index]==userSelection):
                list.pop(index)
                break
        return userSelection,list
    except Exception as ex:
        logging.critical(ex)

list=user_input_to_array()
print(list)
userSelection=input("Select Element to remove its first occurence in list\n")

returnList=remove_first_occurence_specific_element_array(list,userSelection)

print(returnList[1])