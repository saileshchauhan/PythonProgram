'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Take out unique value from Dictionary. 
'''

import logging,logconfig,re

def unique_value_dict(listp):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        listValues=[]
        for dic in listp:
            for values in dic.values():
                listValues.append(values)
        return list(set(listValues))
    except Exception as ex:
        logging.critical(ex)

uniqueValueList=unique_value_dict([{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}])

print(uniqueValueList)

def list_comprehension(list1):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        newList=set([value for dic in list1 for value in dic.values()])
        return list(newList)
    except Exception as ex:
        logging.critical(ex)

uniqueValueListComprehension=list_comprehension([{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}])

print(uniqueValueListComprehension)

