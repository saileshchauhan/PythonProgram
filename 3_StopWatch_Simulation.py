'''
@Author:Sailesh Chauhan
@Date:2021-06-02
@Last Modified by:Sailesh Chauhan
@Last Modified time:8:00 PM
@Title: StopWatch Simulation
'''

import time
try:
    timeList=[]
    def SecondToTimeFormat(second):
        minutes,second=second//60,second%60
        hours,minutes=minutes//60,minutes%60
        return [second,minutes,hours]
    def TimeElapsed():
        input("Press Enter To Start Stop Watch ")
        startTime=time.time()
        input("Press Enter To Stop Stop Watch  ")
        stopTime=time.time()
        return (stopTime-startTime)

    timeList=SecondToTimeFormat(TimeElapsed())
    print("Time Elapsed {0}::{1}::{2} ".format(timeList[2],timeList[1],timeList[0]))
except Exception as ex:
    print(ex.__class__)