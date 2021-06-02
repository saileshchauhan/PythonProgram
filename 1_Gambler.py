'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: Gambler Program
'''

import sys
import random
try:
    win,loose,gameCount=1,0,0
    stackAmount,goal=10,15
    while(0<stackAmount<goal):
        result=random.randint(0,1)
        if(result==win):
            stackAmount+=1
            gameCount+=1
        elif(result==loose):
            stackAmount-=1
            gameCount+=1
    print("Game Count ",gameCount," current Amount ",stackAmount)
except Exception as ex:
    print(ex.__class__)