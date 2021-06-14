'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title:Flip Coin and Print Percentage of Head and Tail
'''

import sys
import random
headCount=tailCount=0

try:
    while True:
        timesToFlipCoin=int(input("Enter count to Flip Coin\n"))
        if(timesToFlipCoin<=0):
            print("Wrong Input Enter 1 or more")
            continue
        break
    for count in range(0,timesToFlipCoin):
        flipCoinResult=random.randint(0,1)
        if(flipCoinResult==0):
            headCount+=1
        elif(flipCoinResult==1):
            tailCount+=1
    print("Percentage of Head Occurence ",int((headCount/timesToFlipCoin)*100))
    print("Percentage of Tail Occurence ",int((tailCount/timesToFlipCoin)*100))
except Exception as ex:
    print(ex.__class__)
    




