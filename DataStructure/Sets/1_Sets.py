'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Create set
'''

#Importing From LogConfig logging config
import logconfig
import logging

def create_set():
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        defaultSet=set()
        choice=''
        print("Ener any number of values to enter in array")
        while(choice.lower()!='q'):
            userValue=input("Enter value\n")
            defaultSet.add(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return set
    except Exception as ex:
        logging.critical(ex)

print_set()




