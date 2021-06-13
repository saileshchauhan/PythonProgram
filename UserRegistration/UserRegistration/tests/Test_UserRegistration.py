import pytest
from lib.RegexPattern import RegexPattern

class Test_Pytest_UserRegistration:

    def test_firstName(self):
        result=RegexPattern.validate_firstName(RegexPattern,"Sailesh")
        assert result==True

    def test_lastName(self):
        result=RegexPattern.validate_lastName(RegexPattern,"Obama")
        assert result==True



