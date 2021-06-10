'''
@Author:Sailesh Chauhan
@Date:2021-06-10
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-10
@Title: Copy list and remove duplicate element from list.
'''

import logconfig
import logging,copy

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

def copy_list(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        copyList=[]
        for item in list:
            copyList.append(item)
        return copyList
    except Exception as ex:
        logging.critical(ex)

def deep_copy_list(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        deepCopy=copy.deepcopy(list)
        return deepCopy
    except Exception as ex:
        logging.critical(ex)

list=create_list()
print("New copy of list using For Loop ",copy_list(list))
print("New copy of list using Deep Copy method of Copy module ",deep_copy_list(list))

def remove_duplicates(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        index=0
        end=len(list)
        while(index<end):
            count=index+1
            while(count<end):
                if(list[index]==list[count]):
                    list.remove(list[index])
                    end-=1
                    count-=1
                count+=1
            index+=1 
        return list
    except Exception as ex:
        logging.critical(ex)

noDuplicateList=remove_duplicates(list)
print("List after removing elements ",noDuplicateList)


