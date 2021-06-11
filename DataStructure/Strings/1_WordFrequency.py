'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Get length of string count each alphabet frequency and char replacement.
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
        userValue=validation(input("You can enter any word"))
        return userValue   
    except Exception as ex:
        logging.error(ex)

def validation(stringValue):
    '''
    Description:
        Provides validation for userinput.
    Parameters:
        stringValue it is userinput.
    Returns:
        correctString after validation.
    '''
    try:
        regexName="^[a-zA-Z0-9]{3,}$"
        if(re.match(regexName,stringValue)):
            return stringValue
        print("String Lenght must be more than 3")
    except Exception as ex:
        logging.critical(ex)

def char_frequency(word):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        count=0
        charFrequency={}
        for char in word:
            for index in range(len(word)):
                if(char==word[index]):
                    count+=1
            charFrequency.update({char:count})
    except Exception as ex:
        logging.critical(ex)
