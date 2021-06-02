'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time: 4:00 PM
@Title: Take Input in 2D array and print 2D array
'''

import sys
ROW_OF_MATRIX=2
COLUMN_OF_MATRIX=2
try:
    matrix=[]
    def InputTwoDimensionMatrix():
        '''Take Input into 2D Matrix'''
        for row in range(1,ROW_OF_MATRIX+1):
            rowMatrix=[]
            for column in range(1,COLUMN_OF_MATRIX+1):
                rowMatrix.append(input("Enter value for position {0}{1} of 2D matrix \n".format(row,column)))
            matrix.append(rowMatrix)

    def PrintTwoDimensionMatrix(matrixPrint):
        '''Print Values of 2D Matrix'''
        for row in range(ROW_OF_MATRIX):
            for column in range(COLUMN_OF_MATRIX):
                print(matrixPrint[row][column],end=" ")
            print()
    InputTwoDimensionMatrix()
    PrintTwoDimensionMatrix(matrix)
except Exception as ex:
    print(ex.__class__)