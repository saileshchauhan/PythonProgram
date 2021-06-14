import pytest
from lib.RegexPattern import RegexPattern

class Test_Pytest_UserRegistration:

    emailPass=["abc@yahoo.com","abc100@yahoo.com","abc.100@yahoo.com","abc111@abc.com","abc-100@ABC.net","abc.100@abc.com.au","abc@1.com","abc@gmail.com.com","abc+100@gmail.com"]

    emailFail=["abc","abc123@gmail.a","abc123@.com","abc123@.com.com","abc()*@gmail.com","abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com","abc@gmail.com.1a","abc@gmail.com.aa.au"]


    def test_given_firstName_should_return_True(self):
        result=RegexPattern.validate_firstName(RegexPattern,"Sailesh")
        assert result==True

    def test_given_lastName_should_return_True(self):
        result=RegexPattern.validate_lastName(RegexPattern,"Obama")
        assert result==True
    
    
    




