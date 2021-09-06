'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: PrimeFactorization using Brute Force
'''
import sys
import math
primeFactor=[]
try:
    inputNumber=int(input("Enter Number to check Prime Number\n"))
    if(inputNumber>1):
        while(inputNumber%2==0):
            primeFactor.append(2)
            inputNumber=inputNumber/2
        for count in range(3,int(math.sqrt(inputNumber)),2):
            while(inputNumber%count==0):
                primeFactor.append(count)
                inputNumber=inputNumber/count
        if(inputNumber>2):
            primeFactor.append(inputNumber)
        print("All PrimeFactors ",*primeFactor)
except Exception as ex:
    print(ex)