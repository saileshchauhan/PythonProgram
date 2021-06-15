'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Remove first occurence of specified element in Array.
'''

import logging,re
from array import array
import sys

sys.path.append(r"D:\OOPs\DataStructure")
import logconfig

def user_input_to_array():
    '''
    Description:
        Takes input from user.
    Parameters:
        None.
    Returns:
        arr containing user input.
    '''
    try:
        arr=array('u')
        choice=''
        print("Ener any number of values to enter in array")
        while(choice.lower()!='q'):
            userValue=input("Enter value\n")
            arr.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return arr
    except Exception as ex:
        logging.critical(ex)

def remove_first_occurence_specific_element_array(usrInputArray,userSelection):
    '''
    Description:
        Removes first occurence of specific element from array.
    Parameters:
        User input array and user selection.
    Returns:
        List containing userSelection and userInput Array.
    '''
    try:
        for index in range(len(usrInputArray)-1):
            if(usrInputArray[index]==userSelection):
                usrInputArray.pop(index)
                break
        return userSelection,usrInputArray
    except Exception as ex:
        logging.critical(ex)

usrInputArray=user_input_to_array()
userSelection=input("Select Element to remove its first occurence in list\n")

returnList=remove_first_occurence_specific_element_array(usrInputArray,userSelection)

print(returnList[1])