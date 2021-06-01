'''
@Author:Sailesh Chauhan
@Date:2021-06-01
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-01
@Title:To Welcome User
'''

try:
    userName=str(input("Enter your Full Name\n"))
    userName=userName.replace(" ","")
    if(len(userName)>3):
        print("Hello "+userName+" ,How are you ?")
    else:
        print("User Name must be more than 3 characters")
except:
    print("Enter Full Name in correct Format")
    exit()
