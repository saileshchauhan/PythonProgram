'''
@Author:Sailesh Chauhan
@Date:2021-06-02
@Last Modified by:Sailesh Chauhan
@Last Modified time:8:00 PM
@Title: Gambler Program
'''

import random

WIN,LOOSE=1,0
def userInput():
    '''
    Description:
        Takes Input from User stackAmount and goalAmount
    Parameters:
        No Parameters
    Return:
        two variables stackAmount and goalAmount

    '''
    try:
        stackAmount=int(input("Enter Total Stack Amount in Rupees\n"))
        goalAmount=int(input("Enter goal amount in Rupees\n"))
        return stackAmount,goalAmount
    except Exception as ex:
        print (ex)

def gamblerGame(stackAmount,goalamount):
    gameCount=0
    '''
    Description:
        Player plays till he/she reaches his/her goalAmount or get
        out complete Broke no amount.
    Parameter:
        Takes two Parameters stackAmount and goalAmount.
    Return:
        No return.
    '''
    try:
        while(0<stackAmount<goalamount):
            result=random.randint(0,1)
            if(result==WIN):
                stackAmount+=1
                gameCount+=1
            elif(result==LOOSE):
                stackAmount-=1
                gameCount+=1
        print("Game Count ",gameCount," current Amount ",stackAmount)
    except Exception as ex:
        print(ex)
#Calling function 
input=userInput()
gamblerGame(input[0],input[1])

