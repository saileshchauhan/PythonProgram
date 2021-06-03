'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 2:00 PM
@Title: Euclidian Distance Between origin and Cartesian Co-oridnates  
'''

import math
try:
    def solveQuadraticEqn(a,b,c):
        """This Function returns two roots of Quadratic Equation"""
        delta=math.pow(b,2)-(4*a*c)
        root_1=(-b+math.sqrt(delta))/(2*a)
        root_2=(-b-math.sqrt(delta))/(2*a)
        return [root_1,root_2]
    def validation(value):
        if(len(value)!=0):
            value=float(value)
            return value
        if(len(value)==0):
            print("empty input not allowed")
            quit()


    print("Enter Coeffecient a,b,c of Quadratic Equation")
    coeffecient_a=input("Enter A coffecient of x^2\n")
    coeffecient_a=validation(coeffecient_a)
    coeffecient_b=input("Enter B coffecient of x  \n")
    coeffecient_b=validation(coeffecient_b)
    constant_c=float(input("Enter C constant      \n"))
    constant_c=validation(constant_c)

    solution=solveQuadraticEqn(coeffecient_a,coeffecient_b,constant_c)
    print("Solution 1 Solution 2 ",*solution)
except Exception as ex:
    print(ex)