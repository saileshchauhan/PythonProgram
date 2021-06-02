'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 2:00 PM
@Title: Euclidian Distance Between origin and Cartesian Co-oridnates  
'''

import math
import sys
solution=[]
try:
    def SolveQuadraticEqn(a,b,c):
        """This Function returns two roots of Quadratic Equation"""
        delta=math.pow(b,2)-(4*a*c)
        root_1=(-b+math.sqrt(delta))/(2*a)
        root_2=(-b-math.sqrt(delta))/(2*a)
        return [root_1,root_2]

    print("Enter Coeffecient a,b,c of Quadratic Equation")
    coeffecient_a=float(input("Enter A coffecient of x^2\n"))
    coeffecient_b=float(input("Enter B coffecient of x  \n"))
    constant_c=float(input("Enter C constant         \n"))

    solution=SolveQuadraticEqn(coeffecient_a,coeffecient_b,constant_c)
    print("Solution 1 Solution 2 ",*solution)
except Exception as ex:
    print(ex.__class__)