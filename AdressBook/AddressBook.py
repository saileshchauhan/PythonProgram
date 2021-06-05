'''
@Author:Sailesh Chauhan
@Date:2021-06-04
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-04
@Title:AddressBook using Object Oriented Approach
'''
import json
import logging

logging.basicConfig(filename='adresBook.log',level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

class Contact:
    '''
    Description:
        Name of class is Contact provides blue print to create custom object
        with attributes firstName,lastName,city,contact
    Function:
        No Function.
    '''
    def __init__(self,firstName,lastName,city,contact):
        self.firstName=firstName
        self.lastName=lastName
        self.city    =city
        self.contact =contact
        pass

def addContact():
    '''
    Description:
        Creates contact of type Contact convert contact object to dictionary
        type and add that object to Json file as JSON.
    Parameters:
        No parameters.
    Return:
        No return
    '''
    try:
        contact=Contact(input("Enter First Name\n"),input("Enter Last Name\n"),input("Enter City Name\n"),input("Enter Contact Number\n"))
        addressBookDict={contact.firstName:contact.__dict__}
        with open('AdressBook.json','w') as file:
            file.write(json.dumps(addressBookDict,indent=4))
    except Exception as ex:
        logging.critical(ex)

def updateContact():
    '''
    Description:
        Method adds new contact type to existing JSON file.
    Parameters:
        No parameters
    Return:
    '''
    try:
        contact=Contact(input("Enter First Name\n"),input("Enter Last Name\n"),input("Enter City Name\n"),input("Enter Contact Number\n"))
        with open('AdressBook.json','+r') as file:
            alreadyExistingContact=json.load(file)
            alreadyExistingContact.update({contact.firstName:contact.__dict__})
            file.seek(0)
            json.dump(alreadyExistingContact,file,indent=4)
            file.close()
    except Exception as ex:
        logging.critical(ex)


def printContact():
    '''
    Description:
        Prints content of JSON file on console.
    Parameters:
        No Parameters.
    Return:
    '''
    try:
        with open('AdressBook.json','+r') as file:
            alreadyExistingContact=json.load(file)
            for contact in alreadyExistingContact.values():
                for key,value in contact.items():
                    print(key+" "+value)
    except Exception as ex:
        logging.critical(ex)

def deleteContact():
    '''
    Description:
        Method deletes JSON object after loading it from JSON. It allows user
        delete particular contact. 
    Parameters:
        No Parameters.
    Return:
    '''
    try:
        with open('AdressBook.json','+r') as file:
            alreadyExistingContact=json.load(file)
            for keys in alreadyExistingContact.keys():
                print("All contact firstName "+keys)
            entryToDelete=input("Enter name of entry to delete\n")
            for keys in alreadyExistingContact.keys():
                if(keys==entryToDelete):
                    print("person found in AdressBook "+keys)
                    entryToDelete=keys
                    print("Entry Removed "+entryToDelete)
                    break
                print("No such person exit in Adressbook")
            del alreadyExistingContact[entryToDelete]
            file.seek(0)
            json.dump(alreadyExistingContact,file,indent=4)
            file.truncate()
            file.close()
    except Exception as ex:
        logging.critical(ex)
    
def main():
    '''
    Description:
        Main method used to call all feature functions.
    Parameters:
        No parameters.
    Return:
    '''
    try:
        choice=""
        while(choice!='5'):
            print("1.Add/Create Contact to AdressBook\n2.Update Contact to AddressBook\n3.Delete Contact from AddressBook\n4.Print All Contact in AddressBook\n5.Quit AdressBook")
            choice=input("Select your option\n")
            if(choice=='1'):
                addContact()
            elif(choice=='2'):
                updateContact()
            elif(choice=='3'):
                deleteContact()
            elif(choice=='4'):
                printContact()
        print("Exited from AddressBook")
    except Exception as ex:
        logging.critical(ex)
if __name__=="__main__":
    main()