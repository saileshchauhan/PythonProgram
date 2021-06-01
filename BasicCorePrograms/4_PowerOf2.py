'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title:Power of two
'''
try:
    CONSTANT,POWER=2,1
    inputNumber=int(input("Enter the Power Value N"))
    if(0<=inputNumber and inputNumber<31):
            for count in range(0,inputNumber):
                while(CONSTANT**POWER <= CONSTANT**inputNumber):
                    print(CONSTANT**POWER)
                    POWER+=1
except:
    print("Invalid Input Enter zero or more")
    exit()

