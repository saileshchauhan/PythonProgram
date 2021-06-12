'''
@Author:Sailesh Chauhan
@Date:2021-06-11
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-11
@Title: Add key to dictionary.
'''

import logging,logconfig

def add_key_to_dict(dict1,dict2,dict3):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        dictk={}
        for d in (dict1,dict2,dict3):
            dictk.update(d)
        return dictk
    except Exception as ex:
        logging.critical(ex)

dictNew=add_key_to_dict({1:20},{2:10},{3:30})

def iterate_dictionary(dict):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        for item in dict.items():
            logging.debug(item)
    except Exception as ex:
        logging.critical(ex)

iterate_dictionary(dictNew)

