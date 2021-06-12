'''
@Author:Sailesh Chauhan
@Date:2021-06-12
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-12
@Title: Covert word to key value pair in Dictionary. With each alphabet count as
        value.
'''

#Importing logConfig for error logging
import logconfig
import logging,re

def create_string():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        userValue=validation(input("You can enter any word\n"))
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
        regexName="^[a-zA-Z0-9,.]{3,}[a-zA-Z]+$"
        if(re.match(regexName,stringValue)):
            return stringValue
        logging.debug("String Lenght must be more than 3")
    except Exception as ex:
        logging.critical(ex)

def char_frequency(word):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        charFrequency={}
        for char in word:
            count=0
            for index in range(len(word)):
                if(char==word[index]):
                    count+=1
            charFrequency.update({char:count})
        return charFrequency
    except Exception as ex:
        logging.critical(ex)

print(char_frequency(create_string()))