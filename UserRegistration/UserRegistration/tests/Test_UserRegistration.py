'''
@Author:Sailesh Chauhan
@Date:2021-06-13
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-13
@Title: User Registration pytest methods.
'''

import pytest
from lib.userRegistration import UserRegistration

class Test_Pytest_UserRegistration:

    emailPass=["abc@yahoo.com","abc-100@yahoo.com","abc100@yahoo.com","abc.100@yahoo.com","abc111@abc.com","abc-100@ABC.net","abc.100@abc.com.au","abc@gmail.com.com","abc+100@gmail.com"]

    emailFail=["abc","abc123@gmail.a","abc123@.com","abc123@.com.com","abc()*@gmail.com","abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com","abc@gmail.com.1a","abc@gmail.com.aa.au"]

    def test_given_firstName_should_return_true(self):
        result=UserRegistration.validate_firstName(UserRegistration,"Samuel")
        assert result==True

    def test_given_lastName_should_return_true(self):
        result=UserRegistration.validate_lastName(UserRegistration,"Obama")
        assert result==True
    
    def test_given_mobileNumber_should_return_true(self):
        result=UserRegistration.validate_mobileNumber(UserRegistration,"+912 7878787878")
        assert result==True

    def test_given_pincode_should_return_true(self):
        result=UserRegistration.validate_pincode(UserRegistration,"460551")
        assert result==True
    
    def test_given_password_should_return_true(self):
        result=UserRegistration.validate_password(UserRegistration,"BridzeLabs88&")
        assert result==True

    def test_given_listOfCorrect_email_shoul_return_true(self):
        for email in self.emailPass:
            result=UserRegistration.validate_email(UserRegistration,email)
            assert result==True

    #-------------------------Negative Test Cases--------------------------------------#

    def test_negative_given_listOfIncorrect_email_should_return_false(self):
        for invalidEmail in self.emailFail:
            result=UserRegistration.validate_email(UserRegistration,invalidEmail)
            assert result==False

    def test_negative_given_wrongFirstName_should_return_false(self):
        result=UserRegistration.validate_firstName(UserRegistration,"samuel")
        assert result==False
    
    def test_negative_given_wrongLastName_should_return_false(self):
        result=UserRegistration.validate_firstName(UserRegistration,"obama")
        assert result==False

    
    




