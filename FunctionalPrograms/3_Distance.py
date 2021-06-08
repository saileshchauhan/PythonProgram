'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: Euclidian Distance Between origin and Cartesian Co-oridnates  
'''

import re
import math


def euclidianDistance(x,y):
    """
    Description:
        Method calculates distance between origin and caretsian
        cordinates.
    Parameters:
        Takes two parameters x(co-ordiante) and y(ordinate).
    Return:
        Euclidian distance between origin and given cartesian
        point
    """
    try:
        return math.sqrt(math.pow(x,2)+math.pow(y,2))
    except Exception as ex:
        print(ex)

    #Validation Method
def validation(value):
    '''
    Description:
        Method validates values given as parameters.
    Parameters:
        Takes value as parameter.
    Return:
        value after validating.
    '''
    try:
        regexFloat="^[+-]?([0-9]*[.])?[0-9]+$"
        if(re.match(regexFloat,value)):
            return float(value)
        print("Invalid Input")
        quit()
    except Exception as ex:
        print(ex)
try:  
    inputX_Coordinate=(input("Enter X-coordinate\n"))
    inputX_Coordinate=validation(inputX_Coordinate)
    inputY_Ordinate=(input("Enter Y-coordinate\n"))
    inputY_Ordinate=validation(inputY_Ordinate)
    #Function Call
    print(euclidianDistance(inputX_Coordinate,inputY_Ordinate))
except Exception as ex:
    print(ex)

