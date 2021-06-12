'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Find Longest word in list.
'''

#Importing logConfig for error logging

import logconfig
import logging,re

def create_list():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultList=[]
        choice=''
        print("You can enter any word in List")
        while(choice.lower()!='q'):
            userValue=validation(input("Enter value to add in List\n"))
            defaultList.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return defaultList
    except Exception as ex:
        logging.error(ex)

def validation(stringValue):
    '''
    Description:
        Provides validation for userinput.
    Parameters:
        stringValue it is userinput.
    Returns:
        correctString after converting it to int validation.
    '''
    try:
        regexName="^[a-zA-Z0-9]{1,}$"
        if(re.match(regexName,stringValue)):
            return stringValue
        logging.debug("Invalid Input")
    except Exception as ex:
        logging.critical(ex)

def longest_word_list(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        longestWord=''
        for index in range(len(list)):
            if(len(longestWord)<len(list[index])):
                longestWord=list[index]
        return longestWord
    except Exception as ex:
        logging.critical(ex)

def longest_word_list(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        list.sort()
        return list[len(list)-1],len(list[len(list)-1])
    except Exception as ex:
        logging.critical(ex)


list=create_list()
print(longest_word_list(['choice','456','right']))
print(longest_word_list(['1','345','choice']))