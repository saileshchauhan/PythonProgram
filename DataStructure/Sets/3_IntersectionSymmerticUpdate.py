'''
@Author:Sailesh Chauhan
@Date:2021-06-09
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-09
@Title: Intersection join,symmetric_difference,symmetric_difference_update.
'''

#Importing logConfig for error logging
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
        print("You can enter any value in set")
        while(choice.lower()!='q'):
            userValue=input("Enter value to add in set\n")
            defaultSet.add(userValue)
            print("Do you want to add more values \nPress C to continue\nQ to stop\n")
            choice=input("Enter choice\n")
        return defaultSet
    except Exception as ex:
        logging.error(ex)

print("Enter Values for First Set")
setFirst=create_set()
print("Enter Values for Second Set")
setSecond=create_set()

def set_intersection(setFirst,setSecond):
    '''
    Description:
    Parameters:
    Return:
    '''
    try:
        thirdSet=setFirst.intersection(setSecond)
        print("Third set {} after intersection of first {} and second {} set".format(thirdSet,setFirst,setSecond))
    except Exception as ex:
        logging.error(ex)

def set_union(setFirst,setSecond):
    '''
    Description:
    Parameters:
    Return:
    '''
    try:
        thirdSet=setFirst.union(setSecond)
        print("Third set after Union {} of first {} and Second Set {} ".format(thirdSet,setFirst,setSecond))
    except Exception as ex:
        logging.error(ex)

def set_symmetric_differnce(setFirst,setSecond):
    '''
    Description:
    Parameters:
    Return:
    '''
    try:
        thirdSet=setFirst.symmetric_difference(setSecond)
        print("Third set after differnce {} of first {} and Second Set {} ".format(thirdSet,setFirst,setSecond))
    except Exception as ex:
        logging.error(ex)

set_intersection(setFirst,setSecond)
set_union(setFirst,setSecond)
set_symmetric_differnce(setFirst,setSecond)