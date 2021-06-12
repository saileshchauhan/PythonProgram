'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Calendar for given month.
'''

import logging
from decouple import config
import calendar

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def print_given_month_year(year,month):
    '''
    Description:
    Parameter:
    Return:
    '''
    try:
        return calendar.month(year,month)
    except Exception as ex:
        logging.critical(ex)

print(print_given_month_year(int(input("Enter year in YYYY\n")),int(input("Enter month \n"))))
