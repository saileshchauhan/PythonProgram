'''
@Author:Sailesh Chauhan
@Date:2021-06-12
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-12
@Title: Count values associated with key in dictionary.
'''

#Importing logConfig for error logging
import logconfig
import logging

def count_values(listDictionary):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        count=0
        for item in listDictionary:
            if True in item.values():
                count+=1
        return count
    except Exception as ex:
        logging.critical(ex)

# countTrue=count_values([{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success':False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}])
# print(countTrue)

#Solving same problem using List Comprehension.

def count_values_listComprehension(listDictionary):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        newList=[x for item in listDictionary for x in item.values() if x==True]
        return newList
    except Exception as ex:
        logging.critical(ex)

list=count_values_listComprehension([{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success':False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}])
print(list)
