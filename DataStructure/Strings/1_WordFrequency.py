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

def char_replacement(word):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        char = word[0]
        word = word.replace(char, '$')
        word = char + word[1:]
        return word
    except Exception as ex:
        logging.critical(ex)

word=create_word()
print(char_replacement(word))
print("word frequency dictionary",char_frequency(word))