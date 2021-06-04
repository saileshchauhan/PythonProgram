'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Take Input in 2D array and print 2D array
'''

import re
def inputRowColumnFor_2DMatrix():
    '''
    Description:
        Takes input from user for row and column of 2D Matrix.
    Parameters:
        No parameters.
    Return:
        List of row and column.
    '''
    try:
        rowSize=input("Enter Required number of rows, only natural number")
        columnSize=input("Enter Required number of columns, only natural number")
        regexNumber="^[1-9]{1,1}[0-9]*$"
        if(re.match(regexNumber,rowSize) and re.match(regexNumber,columnSize)):
            rowSize=int(rowSize)
            columnSize=int(columnSize)
            return rowSize,columnSize
        print("Invalid input ")
        quit()
    except Exception as ex:
        print(ex)
    
def inputTwoDimensionMatrix(ROW_OF_MATRIX,COLUMN_OF_MATRIX):
    '''
    Description:
        Takes input values for position of 2D matrix with not allowing
        empty values.
    Parameters:
        No parameters.
    Return:
        Function return a 2D matrix. 
    '''
    try:
        matrix=[]
        for row in range(1,ROW_OF_MATRIX+1):
            rowMatrix=[]
            for column in range(1,COLUMN_OF_MATRIX+1):
                value=(input("Enter value for position {0}{1} of 2D matrix \n".format(row,column)))
                if(len(value)!=0):
                    rowMatrix.append(value)
            matrix.append(rowMatrix)
        return matrix
    except Exception as ex:
        print(ex)
    
def printTwoDimensionMatrix(matrixPrint,ROW_OF_MATRIX,COLUMN_OF_MATRIX):
    '''
    Description:
        This method Prints a 2D matrix values.
    Parameters:
        This method takes 2D matrix as parameters.
    Return:
        No return.
    '''
    try:
        for row in range(ROW_OF_MATRIX):
            for column in range(COLUMN_OF_MATRIX):
                print(matrixPrint[row][column],end=" ")
            print()
    except Exception as ex:
        print(ex)
matrixSize=inputRowColumnFor_2DMatrix()
matrix=inputTwoDimensionMatrix(matrixSize[0],matrixSize[1])
printTwoDimensionMatrix(matrix,matrixSize[0],matrixSize[1])
