import pytest
from lib.userRegistration import UserRegistration

class Test_Pytest_UserRegistration:

    emailPass=["abc@yahoo.com","abc-100@yahoo.com","abc100@yahoo.com","abc.100@yahoo.com","abc111@abc.com","abc-100@ABC.net","abc.100@abc.com.au","abc@gmail.com.com","abc+100@gmail.com"]

    emailFail=["abc","abc123@gmail.a","abc123@.com","abc123@.com.com","abc()*@gmail.com","abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com","abc@gmail.com.1a","abc@gmail.com.aa.au"]


    def test_given_firstName_should_return_True(self):
        result=UserRegistration.validate_firstName(UserRegistration,"Sailesh")
        assert result==True

    def test_given_lastName_should_return_True(self):
        result=UserRegistration.validate_lastName(UserRegistration,"Obama")
        assert result==True
    
    def test_given_mobileNumber_should_return_True(self):
        result=UserRegistration.validate_mobileNumber(UserRegistration,"+912 7878787878")
        assert result==True

    
    
    




