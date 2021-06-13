'''
@Author:Sailesh Chauhan
@Date:2021-06-13
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-13
@Title: User Registration.
'''

#import logConfig
import re,logging

class RegexPattern:

    REGEX_PASSWORD = "^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z0-9]*)$"
    
    REGEX_EMAIL = "^[a-z0-9A-Z]+([./*$#%][a-zA-Z0-9]{1,})?[@][a-zA-Z]{2,}[.][a-zA-Z]{2,}([.][a-zA-Z]{2})?$"


    def validate_firstName(self,firstName):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            regex_firstName = "^[A-Z]{1}[a-z]{2,}$"
            if(re.match(regex_firstName,firstName)):
                return True
        except Exception as ex:
            logging.critical(ex)
    
    def validate_lastName(self,lastName,regex_lastName="^[A-Z]{1}[a-z]{2,}$"):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            if(re.match(regex_lastName,lastName)):
                return True
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
    
    def validate_pincode(self,pincode,regex_pincode="^[1-9]{1}[0-9]{2,2}[ ]?[0-9]{3}$"):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            return re.match(pincode,regex_pincode)
        except Exception as ex:
            logging.critical(ex)
    
    def validate_password(self,password,regex_password="^[1-9]{1}[0-9]{2,2}[ ]?[0-9]{3}$"):
        '''
        Description:
        Parameters:
        Returns:
        '''
        try:
            return not re.match(password,regex_password)
        except Exception as ex:
            logging.critical(ex)
        pass

# regex=RegexPattern()
# print(regex.validate_firstName("sailesh"))
