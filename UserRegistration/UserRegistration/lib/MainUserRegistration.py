'''
@Author:Sailesh Chauhan
@Date:2021-06-14
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-14
@Title: User Registration main class.
'''

from UserRegistration import logConfig
import re,logging
from userRegistration import UserRegistration

class UserRegistrationMain:

    user=UserRegistration()

    switcher={
    '1':user.validate_firstName,
    '2':user.validate_lastName,
    '3':user.validate_mobileNumber,
    '4':user.validate_pincode,
    '5':user.validate_password,
    '6':user.validate_email
    }

    def switcher_to_call_Methods(choice,switcher,userInput):
        if(choice in ['1','2','3','4','5','6']):
            function=switcher.get(choice)
            return function(userInput)
        return "Invalid Input"

    choice=''
    while(choice.lower()!='q'):
        print("==================User Registration Validation====================")
        print('1.Validate First Name\n2.Validate Last Name\n3.Validate Mobile Number')
        print('4.Validate Pin Code\n5.Validate Password\n6.Validate E-mail')
        choice=input('Enter Key\n')
        
        print(switcher_to_call_Methods(choice,switcher,input("Enter Validation Name")))
        print("Enter Any key to continue\nENTER Q TO STOP PROGRAM")
        choice=input('Enter your choice\n')
