'''
@Author:Sailesh Chauhan
@Date:2021-06-10
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-10
@Title: Copy list and remove duplicate element from list.
'''

import logconfig
import logging

def create_list():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultList=[]
        choice=''
        print("You can enter any value in set")
        while(choice.lower()!='q'):
            userValue=input("Enter value to add in set\n")
            defaultList.append(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return defaultList
    except Exception as ex:
        logging.error(ex)

def long_word_than_given_length(list,size):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        newList=[]
        for item in list:
            if(len(item)>size):
                newList.append(item)
        return newList
    except Exception as ex:
        logging.critical(ex)