'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 2:00 PM
@Title: Euclidian Distance Between origin and Cartesian Co-oridnates  
'''

import math
import re

def solveQuadraticEqn(a,b,c):
    '''
    Description:
        Used to solve quadratic equation.
    Parameters:
        coeffecients of quadratic equation a, b and c.
    Return:
        List of two solutions root 1 and root 2.
    '''
    try:
        delta=math.pow(b,2)-(4*a*c)
        root_1=(-b+math.sqrt(delta))/(2*a)
        root_2=(-b-math.sqrt(delta))/(2*a)
        return [root_1,root_2]
    except Exception as ex:
        print(ex)

def validation(value):
    '''
    Description:
        method validates the input value to eleminate empty input
        incorrect input.
    Parameters:
        Value to be validated for required logic.
    Return:
        value after validating
    '''
    try:
        REGEX_FLOAT="^[+-]?([0-9]*[.])?[0-9]+$"
        if(re.match(REGEX_FLOAT,value)):
            return float(value)
        print("Invalid Input")
        quit()
    except Exception as ex:
        print(ex)

print("Enter Coeffecient a,b,c of Quadratic Equation")
coeffecient_a=input("Enter A coffecient of x^2\n")
coeffecient_a=validation(coeffecient_a)
coeffecient_b=input("Enter B coffecient of x  \n")
coeffecient_b=validation(coeffecient_b)
constant_c=(input("Enter C constant      \n"))
constant_c=validation(constant_c)
#Calling Functions
solution=solveQuadraticEqn(coeffecient_a,coeffecient_b,constant_c)
print("Solution 1 Solution 2 ",*solution)
