'''
@Author:Sailesh Chauhan
@Date:2021-06-13
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-13
@Title: User Registration.
'''

from UserRegistartion import logConfig
import re,logging

class RegexPattern:

    REGEX_PASSWORD = "^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z0-9]*)$"
    REGEX_MOBILE="^[+][0-9]{1,3}[ ][1-9]{1}[0-9]{9}$"
    REGEX_EMAIL = "^[a-z0-9A-Z]+([./*$#%][a-zA-Z0-9]{1,})?[@][a-zA-Z]{2,}[.][a-zA-Z]{2,}([.][a-zA-Z]{2})?$"
    REGEX_LASTNAME = "^[A-Z]{1}[a-z]{2,}$"
    
    REGEX_PINCODE = "^[1-9]{1}[0-9]{2,2}[ ]?[0-9]{3}$"

    def validate_firstName(self,firstName,regex_firstName = "^[A-Z]{1}[a-z]{2,}$"):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            return re.match(firstName, regex_firstName)
        except Exception as ex:
            logging.critical(ex)
    
    def validate_lastName(self,lastName,regex_lastName="^[A-Z]{1}[a-z]{2,}$"):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            return re.match(lastName,regex_lastName)
        except Exception as ex:
            logging.critical(ex)

    def validate_mobileNumber(self,lastName,regex_mobileNumber="^[+][0-9]{1,3}[ ][1-9]{1}[0-9]{9}$"):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            return re.match(lastName,regex_mobileNumber)
        except Exception as ex:
            logging.critical(ex)
    pass

