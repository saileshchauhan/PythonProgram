'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Sum of three integers add to zero
'''
import sys
try:
    numberList=[1,3,-4,3,2,1]
    def FindThreeIntegersAddToZero():
        '''Print three integers adding to Zero'''
        for firstPlace in range(len(numberList)-2):
            for secondPlace in range(firstPlace+1,(len(numberList)-1)):
                for thirdPlace in range(secondPlace+1,len(numberList)):
                    if((numberList[firstPlace]+numberList[secondPlace]+numberList[thirdPlace])==0):
                        print(numberList[firstPlace],numberList[secondPlace],numberList[thirdPlace])
        return 1
 #Implemented Main definition only for practise       
    def main():
        flag=0
        flag=FindThreeIntegersAddToZero()
        if(flag==0):
            print("No three integers add to zero")
    if __name__=="__main__":
        main()
except Exception as ex:
    print(ex.__class__)