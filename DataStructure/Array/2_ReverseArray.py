'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Array values after reversing order.
'''

import array
import logging
from DataStructure import logconfig

def reverseArray(array):
    '''
    Description:
    Parameters:
    Return:
    '''
    count=(len(array)-1)
    length=len(array)//2
    for index in range(length):
        temp=array[index]
        array[index]=array.pop(count)
        array.insert(count,temp)
        count-=1
    return array        

strArray=array.array('u',('a','b','c','d','e'))
print(reverseArray(strArray))

def reverseArrayWhile(array):
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
    return array

intArray=array.array('i',(1,2,3,4,5))
print(reverseArrayWhile(intArray))