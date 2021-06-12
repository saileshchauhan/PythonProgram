'''
@Author:Sailesh Chauhan
@Date:2021-06-12
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-12
@Title: Write a Python program to check multiple keys exists in a dictionary.
'''

#Importing logConfig for error logging
import logconfig
import logging

def check_multipleKey_exist_in_dict(dict1,keySet1,keySet2):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        return keySet1.issubset(dict1.keys()),keySet2.issubset(dict1.keys())
    except Exception as ex:
        logging.critical(ex)

keyValuePair = {"sam" : 1, "sandra" : 2, "mike" :3}
keySet = set(['sam', 'sandra'])
keySetnot = set(['sandra','billi'])

returnList=check_multipleKey_exist_in_dict(keyValuePair,keySet,keySetnot)

print("%s key in dictionary %s is subset return %s "%(keySet,keyValuePair.keys(),returnList[0]))
print("%s all key not in dictionary %s is subset return %s "%(keySetnot,keyValuePair.keys(),returnList[1]))