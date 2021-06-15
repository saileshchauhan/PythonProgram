'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Number of occurence of specified element in Array.
'''

import sys
from array import array
import logging,re

sys.path.append(r"D:\OOPs\DataStructure")
import logconfig



def user_input_to_array():
    '''
    Description:
        Takes input from user into array.
    Parameters:
        No parameters.
    Returns:
        strArray which stores input from user.
    '''
    try:
        strArray=array('u')
        choice=''
        print("Ener any number of values to enter in array")
        while(choice.lower()!='q'):
            userValue=input("Enter value\n")
            strArray.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return strArray
    except Exception as ex:
        logging.critical(ex)
        
        
def occurence_of_specific_element_array(inputArray,userSelection):
    '''
    Description:
        Method finds count of user selected element in the array.
    Parameters:
        Takes array and userselection.
    Returns:
        userSelection and count.
    '''
    count=0
    for index in range(len(inputArray)):
        if(inputArray[index]==userSelection):
            count+=1
    return userSelection,count

arr=user_input_to_array()

userSelection=input("Select Element to count its occurence in list\n")

returnList=occurence_of_specific_element_array(arr,userSelection)

print("Selected element %s Occurence count %s " %(returnList[0],returnList[1]))
