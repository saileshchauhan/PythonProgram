'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: Euclidian Distance Between origin and Cartesian Co-oridnates  
'''

import sys
import math
try:

    def euclidianDistance(x,y):
        """This Function returns Euclidian Distance"""
        return math.sqrt(math.pow(x,2)+math.pow(y,2))
    def Validation(value):
        if(len(value)!=0):
            value=float(value)
            return value
        if(len(value)==0):
            print("empty input not allowed")
            quit()

    inputX_Coordinate=(input("Enter X-coordinate\n"))
    inputX_Coordinate=Validation(inputX_Coordinate)
    inputY_Ordinate=(input("Enter Y-coordinate\n"))
    inputY_Ordinate=Validation(inputY_Ordinate)

    print(euclidianDistance(inputX_Coordinate,inputY_Ordinate))
except Exception as ex:
    print(ex)
except TypeError:
    print("Enter Valid Input")

