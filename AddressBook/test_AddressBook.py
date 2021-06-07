'''
@Author:Sailesh Chauhan
@Date:2021-06-07
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-07
@Title:AddressBook using Object Oriented Approach
'''

import unittest
import AddressBook

class Test_AddressBook(unittest.TestCase):

    def test_addContact(self):
        '''
        Description:
            This method asserts as entered contact name is 
            updated as key in addressBookDict Dictionary.
        Parameters:
            self. It refers to object of this class which is
            passed as unittest.TestCase. 
        TestOutcome:
            checks if the entered contact is existing in addressBookDict.
            Used Assert for that.
        '''
        listReturn=AddressBook.addContact()
        contact=listReturn[0]
        contactFirstName=contact.firstName
        addressBookDict=listReturn[1]
        #Test Body
        if contactFirstName in addressBookDict:
            result=True
        assert result==True
    def test_verify_entries(self):
        '''
        Description:
            This method asserts as entered contact details such as
            firstName,lastName,etc. is stored corresponding to correct
            key which is user firstName.
        Parameters:
            self
        Return:
        '''
        listReturn=AddressBook.addContact()
        contact=listReturn[0]
        contactFirstNameAsKey=contact.firstName
        addressBookDict=listReturn[1]
        #Test Body
        assert addressBookDict[contactFirstNameAsKey]==contact.__dict__

if __name__=="__main__":
    unittest.main()
