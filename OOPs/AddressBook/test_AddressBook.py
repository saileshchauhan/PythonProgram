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
    '''
    Description:
        Unit Test Class to complete testing of AddressBook 
        methods.
    TestMethods:
        1. test_addContact.
        2. test_verify_entries.
    '''

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

    def test_verify_entry_deletes(self):
        '''
        Description:
            This method asserts if deleted contact has been removed.
            From the AddressBook. IF removed than asserts true.
        Parameters:
            self
        Return:
            None.
        '''
        listReturn=AddressBook.deleteContact()
        entryToDelete=listReturn[0]
        addressBookDict=listReturn[1]
        check=addressBookDict.get(entryToDelete,"not found")
        assert check=="not found"
        
if __name__=="__main__":
    unittest.main()
