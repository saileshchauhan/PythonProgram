'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: PrimeFactorization using Brute Force
'''
import sys
primeFactor=[]
try:
    inputNumber=int(input("Enter Number to check Prime Number\n"))
    if(inputNumber>1):
        while(inputNumber%2==0):
            primeFactor.append(2)
            inputNumber=inputNumber/2
        if(inputNumber>1):
            for count in range(3,inputNumber,2):
                while(count*count<=inputNumber and inputNumber%count==0):
                    primeFactor.append(count)
                    inputNumber=inputNumber/count
                break
        if(inputNumber>2):
            primeFactor.append(inputNumber)
        print("prime factors ",*primeFactor)
except Exception as ex:
    print(ex.__class__)