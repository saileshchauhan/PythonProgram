'''
@Author:Sailesh Chauhan
@Date:2021-06-04
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-04
@Title:AddressBook using Object Oriented Approach
'''
import json
from collections import namedtuple
class Contact(object):
    def __init__(self,firstName,lastName,city,contact):
        self.firstName=firstName
        self.lastName=lastName
        self.city    =city
        self.contact =contact
        pass

    def printContactDetails(self):
        return " {} {} {} {} ".format(self.firstName,self.lastName,self.city,self.contact)
def addCOntact():
    try:
        contact=Contact(input("Enter First Name\n"),input("Enter Last Name\n"),input("Enter City Name\n"),input("Enter Contact Number\n"))
        addressBookDict={contact.firstName:contact.__dict__}
        with open('AdressBook.json','+r') as file:
            file.write(json.dumps(addressBookDict,indent=4))
    except Exception as ex:
        print(ex)
#addCOntact()

def updateContact():
    try:
        contact=Contact(input("Enter First Name\n"),input("Enter Last Name\n"),input("Enter City Name\n"),input("Enter Contact Number\n"))
        #addressBookDict={"AddressBook Contact":contact.__dict__}
        with open('AdressBook.json','+r') as file:
            alreadyExistingContact=json.load(file)
            alreadyExistingContact.update({contact.firstName:contact.__dict__})
            file.seek(0)
            json.dump(alreadyExistingContact,file,indent=4)
            file.close()
    except Exception as ex:
        print(ex)
#updateContact()

def printContact():
    try:
        with open('AdressBook.json','+r') as file:
            alreadyExistingContact=json.load(file)
            for contact in alreadyExistingContact.keys():
                print("All contact firstName "+contact)
            for key,value in alreadyExistingContact.values():
                print(key+" "+value)
           # alreadyExistingContact[]
    except Exception as ex:
        print(ex)
# printContact()

def deleteContact():
    try:
        with open('AdressBook.json','+r') as file:
            alreadyExistingContact=json.load(file)
            for keys in alreadyExistingContact.keys():
                print("All contact firstName "+keys)
            entryToDelete=input("Enter name of entry to delete \n")
            for keys in alreadyExistingContact.key():
                if(keys==entryToDelete):
                    print("person found in AdressBook "+keys)
                    del alreadyExistingContact[entryToDelete]
            print("No such person exit in Adressbook")
            file.seek(0)
            json.dump(alreadyExistingContact,file,indent=4)
            file.truncate()
            file.close()
    except Exception as ex:
        print(ex)
#deleteContact()
    

   