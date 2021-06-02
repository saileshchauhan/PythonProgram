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

    def EuclidianDistance(x,y):
        """This Function returns Euclidian Distance"""
        return math.sqrt(math.pow(x,2)+math.pow(y,2))

    inputX_Coordinate=float(input("Enter X-coordinate\n"))
    inputY_Ordinate=float(input("Enter Y-coordinate\n"))
    print(EuclidianDistance(inputX_Coordinate,inputY_Ordinate))
except Exception as ex:
    print(ex.__class__)

