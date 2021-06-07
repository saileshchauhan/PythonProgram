'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title: Harmonic Series
'''
nthNumber=0
try:
    nthTerm=int(input(" Enter nthTerm for Harmonic nth Number\n"))
    for count in range(1,(nthTerm+1)):
        nthNumber+=(1/count)
    print("nthNumber {0} for nthTerm {1}".format(nthNumber,nthTerm))
except Exception as ex:
    print(ex.__class__)
        