'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Take N as key and N*N as value and remove key.
'''

import logging,logconfig,re

def key_N_value_N_sqre(N):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        dict={}
        for n in range(1,N+1):
            key,value=n,n*n
            dict.update({key:value})
        return dict
    except Exception as ex:
        logging.critical(ex)
        
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
        regexName="^[0-9]{1,}$"
        if(re.match(regexName,stringValue)):
            return int(stringValue)
        logging.debug("Invalid Input")
    except Exception as ex:
        logging.critical(ex)

def remove_key(key,dict1):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        del dict1[key]
        return dict1
    except Exception as ex:
        logging.critical(ex)

usrInput=validation(input("Enter N for key value in dictionary\n"))
dict=key_N_value_N_sqre(usrInput)
dict1=remove_key(usrInput,dict)
print(dict1)