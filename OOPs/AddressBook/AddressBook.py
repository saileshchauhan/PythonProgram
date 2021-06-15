'''
@Author:Sailesh Chauhan
@Date:2021-06-04
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-04
@Title:AddressBook using Object Oriented Approach
'''
import json
import logging
from decouple import config 

FILE_NAME=config('File_Name')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

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
    #try:
    contact=Contact(input("Enter First Name\n"),input("Enter Last Name\n"),input("Enter City Name\n"),input("Enter Contact Number\n"))
    if(len(contact.firstName)<3 or len(contact.contact)<10):
        raise ValueError("The firstName should be more than 3")
    addressBookDict={contact.firstName:contact.__dict__}
    return [contact,addressBookDict]
        #For unit testing used return. To use application please
        #remove return line and uncomment line 45 and 46.
        # with open(FILE_NAME,'w') as file:
        #     file.write(json.dumps(addressBookDict,indent=4))
    # except Exception as ex:
    #     logging.critical(ex)

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
        with open(FILE_NAME,'+r') as file:
            alreadyExistingContact=json.load(file)
            alreadyExistingContact.update({contact.firstName:contact.__dict__})
            file.seek(0)
            json.dump(alreadyExistingContact,file,indent=4)
            file.close()
    except Exception as ex:
        logging.critical(ex)

def editContact():
    '''
    Description:
        Allows user to correct already existing contact entry. In AdressBook.
    Parameters:
        No Parameters.
    Return:
    '''
    try:
        with open(FILE_NAME,'+r') as file:
            alreadyExistingContact=json.load(file)
            firstName=input("Enter first Name to edit")
            for key,value in alreadyExistingContact.items():
                if(key==firstName):
                    print("Contact Found "+firstName)
                    value["firstName"]=input("Enter correct Name\n")
                    value["lastName"]=input("Enter correct lastName\n")
                    value["city"]=input("Enter correct cityName\n")
                    value["contact"]=input("Enter correct Contact\n")
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
        with open(FILE_NAME,'+r') as file:
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
        with open(FILE_NAME,'+r') as file:
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
            return [entryToDelete,alreadyExistingContact]
            # file.seek(0)
            # json.dump(alreadyExistingContact,file,indent=4)
            # file.truncate()
            # file.close()
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
        while(choice!='6'):
            print("1.Add/Create Contact to AddressBook\n2.Update Contact to AddressBook")
            print("3.Delete Contact from AddressBook\n4.Print All Contact in AddressBook")
            print("5.Edit AdressBook\n6.Exit AdressBook")
            choice=input("Select your option\n")
            if(choice=='1'):
                addContact()
            elif(choice=='2'):
                updateContact()
            elif(choice=='3'):
                deleteContact()
            elif(choice=='4'):
                printContact()
            elif(choice=='5'):
                editContact()
        print("Exited from AddressBook")
    except Exception as ex:
        logging.critical(ex)
if __name__=="__main__":
    main()