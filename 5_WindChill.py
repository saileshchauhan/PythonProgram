'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Wind Chill using Tempreatur in F and Velocity in milesperHour
'''

import math
import sys
try:
    def WindChill(tempreature,velocity):
        """This function returns WindChill 
        using Temp(F) and velocity(mph)
        function not valid for T greater than 50
        and wind velocity."""
        a=(0.4275*tempreature-35.75)
        b=math.pow(velocity,0.16)
        return (35.74+0.6215*tempreature + a*b)

    tempreature=float(input("Enter Tempreture(in F) less than 50 \n"))
    velocity=float(input("Enter Velocity(in mph) less than 120 \n"))

    print("The wind chill for given Tempreature and Wind Velocity ",WindChill(tempreature,velocity))
    
except Exception as ex:
    print(ex.__class__)
