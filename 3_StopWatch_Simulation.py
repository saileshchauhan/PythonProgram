'''
@Author:Sailesh Chauhan
@Date:2021-06-02
@Last Modified by:Sailesh Chauhan
@Last Modified time:8:00 PM
@Title: StopWatch Simulation
'''

import time
timeList=[]
def SecondToTimeFormat(second):
    '''
    Description:
        Convert second to Time format HH:MM:SS
    Parameter:
        seconds
    Return:
        List of seconds,minutes,hours
    '''
    try:
        minutes,second=second//60,second%60
        hours,minutes=minutes//60,minutes%60
        return [second,minutes,hours]
    except Exception as ex:
        print(ex)

def TimeElapsed():
    '''
    Description:
        Calculates time elapsed between start and stop for stop watch
    Parameters:
        No Parameters
    Return:
        Difference between start and stop
    '''
    try:
        input("Press Enter To Start Stop Watch ")
        startTime=time.time()
        input("Press Enter To Stop Stop Watch  ")
        stopTime=time.time()
        return (stopTime-startTime)
    except Exception as ex:
        print(ex)

timeList=SecondToTimeFormat(TimeElapsed())
print("Time Elapsed {0}::{1}::{2} ".format(timeList[2],timeList[1],timeList[0]))
