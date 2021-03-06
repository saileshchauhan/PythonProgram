'''
@Author:Sailesh Chauhan
@Date:2021-06-13
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-13
@Title: User Registration.
'''

#import logConfig
import re,logging

class UserRegistration:

    regex_pincode="^[1-9]{1}[0-9]{2,2}[ ]?[0-9]{3}$"
    regex_mobileNumber="^[+][0-9]{1,3}[ ][1-9]{1}[0-9]{9}$"
    regex_lastName="^[A-Z]{1}[a-z]{2,}$"
    regex_firstName = "^[A-Z]{1}[a-z]{2,}$"
    regex_password="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    regex_email= "^[a-z0-9A-Z]+([-+.$#%][a-zA-Z0-9]{1,})?[@][a-zA-Z0-9]{2,}[.][a-zA-Z]{2,}([.][a-zA-Z]{2,})?$"


    def validate_firstName(self,firstName):
        '''
        Description:
            Method validates first Name.
        Parameters:
            self and firstName.
        Returns:
            Bool values True or False
        '''
        try:
            if(re.match(self.regex_firstName,firstName)):
                return True
            return False
        except Exception as ex:
            logging.critical(ex)
    
    def validate_lastName(self,lastName):
        '''
        Description:
            Method validates last Name.
        Parameters:
            self and last name.
        Returns:
            Bool values True or False
        '''
        try:
            if(re.match(self.regex_lastName,lastName)):
                return True
            return False
        except Exception as ex:
            logging.critical(ex)

    def validate_mobileNumber(self,mobileNumber):
        '''
        Description:
            Method validates mobile number.
        Parameters:
            self and mobile number.
        Returns:
            Bool values True or False.
        '''
        try:
            if(re.match(self.regex_mobileNumber,mobileNumber,)):
                return True
            return False
        except Exception as ex:
            logging.critical(ex)
    
    def validate_pincode(self,pincode):
        '''
        Description:
            Method validates pincode.
        Parameters:
            self and pincode.
        Returns:
            Bool values True or False
        '''
        try:
            if(re.match(self.regex_pincode,pincode)):
                return True
            return False
        except Exception as ex:
            logging.critical(ex)
    
    def validate_password(self,password):
        '''
        Description:
            Method validates password.
        Parameters:
            self and password.
        Returns:
            Bool values True or False
        '''
        try:
            if(re.match(self.regex_password,password)):
                return True
            return False
        except Exception as ex:
            logging.critical(ex)
        pass

    def validate_email(self,email):
        '''
        Description:
            Method validates email.
        Parameters:
            self and e-mail.
        Returns:
            Bool values True or False
        '''
        try:
            if(re.match(self.regex_email,email)):
                return True
            return False
        except Exception as ex:
            logging.critical(ex)



