'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title:Flip Coin and Print Percentage of Head and Tail
'''
import random
headCount=tailCount=0
while True:
    try:
        timesToFlipCoin=int(input("Enter count to Flip Coin"))
        if(timesToFlipCoin<0):
            print("Wrong Input Enter 1 or more")
            continue
        break
    except:
        print("Input is not Number")
        exit()
for count in range(0,timesToFlipCoin):
    flipCoinResult=random.randint(0,1)
    if(flipCoinResult==0):
        headCount+=1
    elif(flipCoinResult==1):
        tailCount+=1
print("Percentage of Head Occurence ",(headCount/timesToFlipCoin)*100)
print("Percentage of Tail Occurence ",(tailCount/timesToFlipCoin)*100)



