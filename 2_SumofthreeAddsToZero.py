'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Sum of three integers add to zero
'''
import sys
try:
    def inputFromUser():
        listOfIntegers=[]
        numOfintegers=int(input("Enter number of integers to add\n"))
        if(numOfintegers<0):
            print("invalid input only whole number allowed")
            quit()
        for count in range(numOfintegers):
            value=int(input("Enter integers\n"))
            listOfIntegers.append(value)
        return listOfIntegers
    def findThreeIntegersAddToZero(list):
        '''Print three integers adding to Zero'''
        for firstPlace in range(len(list)-2):
            for secondPlace in range(firstPlace+1,(len(list)-1)):
                for thirdPlace in range(secondPlace+1,len(list)):
                    if((list[firstPlace]+list[secondPlace]+list[thirdPlace])==0):
                        print(list[firstPlace],list[secondPlace],list[thirdPlace])
        return 1
 #Implemented Main definition only for practise       
    def main():
        flag=0
        numberList=inputFromUser()
        flag=findThreeIntegersAddToZero(numberList)
        if(flag==0):
            print("No three integers add to zero")
    if __name__=="__main__":
        main()
except ValueError:
    print("Only Integers are allowed")
except TypeError:
    print("Enter Valid Input")
except Exception as ex:
    print(ex)