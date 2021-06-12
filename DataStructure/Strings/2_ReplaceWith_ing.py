'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Add "ing" at the end of the string if present then add ly.
'''

#Importing logConfig for error logging
import logconfig
import logging,re

def create_word():
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
        regexName="^[a-zA-Z0-9.]{3,}[a-zA-Z]+$"
        if(re.match(regexName,stringValue)):
            return stringValue
        logging.debug("String Lenght must be more than 3")
    except Exception as ex:
        logging.critical(ex)

def replace_with_ing_ly(word):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        index=word.find('ing')
        if(len(word)>=3 and index>-1):
            return word+'ly'
        elif(len(word)>=3 and index==-1):
            return word+'ing'
    except Exception as ex:
        logging.critical(ex)

word=create_word()
print("Entered word %s Replaced Word %s "%(word,replace_with_ing_ly(word)))
            