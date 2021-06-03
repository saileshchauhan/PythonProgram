'''
@Author:Sailesh Chauhan
@Date:2021-06-03
@Last Modified by:Sailesh Chauhan
@Last Modified time:9:00 AM
@Title: Total Random Number Generation for Distict Coupoun
'''

import random
try:
    uniqueCouponList=[1,2,3,4]
    newUniqueList=[]
    def RandomNumberCount(list):
        count=0
        while(len(newUniqueList)<len(uniqueCouponList)):
            result=random.randint(0,10)
            count+=1
            if result in uniqueCouponList:
                if result not in newUniqueList:
                    newUniqueList.append(result)
        return count
    print("Random count generated ",RandomNumberCount(uniqueCouponList))
except Exception as ex:
    print(ex.__class__)
