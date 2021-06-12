'''
@Author:Sailesh Chauhan
@Date:2021-06-12
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-12
@Title: Convert list to tuple 
'''

#Importing logConfig for error logging
import logconfig
import logging

def create_list():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultList=list()
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
