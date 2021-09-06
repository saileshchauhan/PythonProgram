'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title:Power of two
'''
import sys
try:
    CONSTANT,power=2,1
    inputNumber=int(input("Enter the Power Value N \n"))
    if(0<=inputNumber and inputNumber<31):
        while(CONSTANT**power <= CONSTANT**inputNumber):
            for count in range(0,inputNumber):
                print(CONSTANT**power)
                power+=1
except Exception as ex:
    print(ex)
    print("Invalid Input Enter zero or more")
    exit()

