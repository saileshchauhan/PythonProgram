'''
@Author:Sailesh Chauhan
@Date:2021-06-03
@Last Modified by:Sailesh Chauhan
@Last Modified time:9:00 AM
@Title: Total Random Number Generation for Distict Coupoun
'''

import random
import re
def userInput(regexPattern):
    '''
    Description:
        Using regex pattern to validate user input 
    Parameter:
        Regex Pattern
    Return:
        number of coupons to be generated
    '''
    try:
        numberOfCoupons=input("Enter Number of unique coupons to be generated\n")
        if(re.match(regexPattern,numberOfCoupons)):
            if(int(numberOfCoupons)<=0):
                print("Input less than 0 ")
                quit()
            return int(numberOfCoupons)
        print("Please enter positive whole number")
        quit()
    except Exception as ex:
        print(ex)
def randomCouponCount(couponCount):
    '''
        Description:
            It finds the count of Random number required to generate unique coupon matching
            with given distinct coupon.
        Parameters:
            uniqueCouponList and newUniqueCouponList
        Return:
            count of random generated number
        '''
    try:
        couponList=[]
        randomCount=ifCouponExist=0
        while(randomCount<couponCount+ifCouponExist):
            coupon=random.randint(1,couponCount)
            randomCount+=1
            if(len(couponList)==0):
                couponList.append(coupon)
                continue
            elif(coupon in couponList):
                ifCouponExist+=1
                continue
            couponList.append(coupon)
        print("Unique Coupon generated ",*couponList)
        return randomCount
    except Exception as ex:
        print(ex)
    
    
REGEX_NUMBER="^[0-9]{1,}$"
print("Random count generated ",randomCouponCount(userInput(REGEX_NUMBER)))