'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Wind Chill using Tempreatur in F and Velocity in milesperHour
'''

import math

def windChill(tempreature,velocity):
    '''
    Description:
        This function returns WindChill 
        using Temp(F) and velocity(mph)
        function not valid for T greater than 50
        and wind velocity.
    Parameters:
        Takes tempreature and velocity as parameters.
    Return:
        function returns wind chill.
    '''
    try:
        a=(0.4275*tempreature-35.75)
        b=math.pow(velocity,0.16)
        return (35.74+0.6215*tempreature + a*b)
    except Exception as ex:
        print(ex)

    #Validation Method
def validation(value1,value2):
    '''
    Desctription:
        Function validates value1 and value2 as required for
        logic of Wind chill.
    Parameters:
        value1 and value2 for validation, as tempreature and
        velocity.
    Return:
        value1 and value2 required for tempreature and velocity.
    '''
    try:
        if(len(value1)!=0 and len(value2)!=0):
            value1,value2=float(value1),float(value2)
            if(value1<50 and value2<120):
                return value1,value2
            print("Invalid Input")
            quit()
        print("empty input not allowed")
        quit()
    except Exception as ex:
        print(ex)

tempreature=(input("Enter Tempreture(in F) less than 50 \n"))
velocity=(input("Enter Velocity(in mph) less than 120 \n"))
tempVelocity=validation(tempreature,velocity)
print("The wind chill for given Tempreature and Wind Velocity ",windChill(tempVelocity[0],tempVelocity[1]))
    
