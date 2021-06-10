'''
@Author:Sailesh Chauhan
@Date:2021-06-09
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Create, Clear, frozen Set function in Sets.
'''

import logconfig,logging,re

def create_set():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        choice=''
        list=[]
        while(choice.lower()!='q'):
            userValue=validation(input("Enter word to be converted into list\n"))
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            list.append(userValue.split(userValue[0]))
            choice=input("Enter choice\n")
        return list
    except Exception as ex:
        logging.error(ex)

def validation(stringValue):
    '''
    Description:
        Provides validation for userinput.
    Parameters:
        stringValue it is uerinput.
    Returns:
        correctString after validation.
    '''
    try:
        regexName="^[a-zA-z]{1,}$"
        if(re.match(regexName,stringValue)):
            return stringValue
        print("Invalid Input")
    except Exception as ex:
        logging.critical(ex)

print("After spliting word into list ",create_set())