'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title:To Welcome User
'''

import sys
try:
    userName=str(input("Enter your Full Name\n"))
    userName=userName.replace(" ","")
    if(len(userName)>3):
        print("Hello "+userName+" ,How are you ?")
        quit()
    print("User Name must be more than 3 characters") 
except Exception as ex:
    print(ex.__class__)