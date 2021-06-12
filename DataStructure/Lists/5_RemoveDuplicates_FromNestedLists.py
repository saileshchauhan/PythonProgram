'''
@Author:Sailesh Chauhan
@Date:2021-06-10
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-10
@Title: Make list of new words greater than given size.
'''

import logconfig
import logging,itertools

def remove_duplicates_from_nested_list(numlist):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        print("Original List", numlist)
        numlist.sort()
        listAfterSorting = list(numlist for numlist,anything in itertools.groupby(numlist))
        return listAfterSorting
    except Exception as ex:
        logging.critical(ex)

print("List After Sortings ",remove_duplicates_from_nested_list([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))