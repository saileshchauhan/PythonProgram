'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print cpu count
'''
import multiprocessing,time
import logging
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def print_cpu_used():
    '''
    '''
    print(multiprocessing.cpu_count())

print_cpu_used()

print(time.strftime("%H:%M:%S"))