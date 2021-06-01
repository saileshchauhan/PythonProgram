'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: Check Leap year
'''
try:
    year=int(input("Enter Year in YYYY\n"))
    year=str(year)
    if(len(year)==4):
        if(int(year)%400==0):
            print("Leap Year {0} ".format(year))
        elif(int(year)%4==0 and int(year)%100!=0):
            print("Leap Year {0} ".format(year))
    else:
        print("Enter in YYYY format")
except:
    print("Input should be a positive Integer")
