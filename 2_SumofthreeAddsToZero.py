'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Sum of three integers add to zero
'''


def inputFromUser():
    '''
    Description:
        Takes integer as input for array of integers and validate
        user input should not be less than 1
    Parameters:
        No parameters
    Return:
        If returns a list of Integers
    '''
    try:
        listOfIntegers=[]
        numOfintegers=int(input("Enter number of integers to add\n"))
        #Validation
        if(numOfintegers<0):
            print("invalid input only whole number allowed")
            quit()
        for count in range(numOfintegers):
            value=int(input("Enter integers\n"))
            listOfIntegers.append(value)
        return listOfIntegers
    except Exception as ex:
        print(ex)
def findThreeIntegersAddToZero(list):
    '''
    Description:
        Takes list of Integers and find triplet of integers which
        adds to zero.
    Parameters:
        list of integers 
    Return:
        This function returns flag value
    '''
    try:
        for firstPlace in range(len(list)-2):
            for secondPlace in range(firstPlace+1,(len(list)-1)):
                for thirdPlace in range(secondPlace+1,len(list)):
                    if((list[firstPlace]+list[secondPlace]+list[thirdPlace])==0):
                        print(list[firstPlace],list[secondPlace],list[thirdPlace])
        return 1
    except Exception as ex:
        print(ex)
 #Implemented Main definition     
def main():
    '''
    Description:
        It gives entry point to program. If is used to call other definition
        in program code.
    Parameters:
        Do not take any parameters.
    Return:
        No return type.
    '''
    try:
            
        flag=0
        numberList=inputFromUser()
        flag=findThreeIntegersAddToZero(numberList)
        if(flag==0):
            print("No three integers add to zero")
        if __name__=="__main__":
            main()
    except Exception as ex:
        print(ex)
