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

def list_to_nestedKey_value_dict(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        dict={}
        for index in range(len(list)):
            dict.update({list[index]:list[index+1:len(list)+1]})
        return dict
    except Exception as ex:
        logging.critical(ex)

dict=list_to_nestedKey_value_dict([1,2,3,4,5,6])
print(dict)

def list_to_nestedKey_dict(list):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
	    newDictinonary = current = {}
	    for key in list:
	        current[key] = {}
	        current = current[key]
	    return newDictinonary
    except Exception as ex:
        logging.critical(ex)

nestedKeyDict=list_to_nestedKey_dict(['s','a','b'])
print(nestedKeyDict)