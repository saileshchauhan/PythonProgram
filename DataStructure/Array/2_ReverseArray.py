'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Array values after reversing order.
'''

import logging
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

def reverseArray(array):
    '''
    Description:
    Parameters:
    Return:
    '''
    count=len(array)-1
    length=len(array)//2
    for index in range(length):
        temp=array[index]
        array[index]=array[count]
        array[count]=temp
        count-=1
    print(array)

reverseArray(['a','b','c','d'])

def reverseArray(array):
    '''
    Description:
    Parameters:
    Return:
    '''
    start=0
    end=len(array)-1
    while(start<end):
        array[start],array[end]=array[end],array[start]
        start+=1
        end-=1
    print(array)

reverseArray([1,2,3,4,5])