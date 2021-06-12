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

def longest_word_list(list1):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        longestWord=''
        for index in range(len(list1)):
            if(len(longestWord)<len(list1[index])):
                longestWord=list1[index]
        return longestWord
    except Exception as ex:
        logging.critical(ex)

def longest_word_list_another(list2):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        list2.sort()
        return list2[len(list2)-1],len(list2[len(list2)-1])
    except Exception as ex:
        logging.critical(ex)


listParameter=create_list()
print(longest_word_list(listParameter))
print(longest_word_list_another(listParameter))