'''
@Author:Sailesh Chauhan
@Date:2021-06-05
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-05
@Title:Inventory Management 
'''
import json
import logging
from decouple import config 

FILE_PATH_LOG=config('log_File_Path')
FILE_PATH_JSON=config('json_File_Path')

logging.basicConfig(filename=FILE_PATH_LOG,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')


class Inventory:
    '''
    Description:
        Name of class is Contact provides blue print to create custom object
        with attributes firstName,lastName,city,contact
    Function:
        No Function.
    Variables:
        Class Variables Name,Weight,PricePerKg.
    '''
    def __init__(self,name,weight,pricePerKg):
        self.name=name
        self.weight=weight
        self.pricePerKg=pricePerKg
        pass

inventoryDict={}
def load_JSON_to_dictionary():
    global inventoryDict
    with open(FILE_PATH_JSON,'+r') as file:
            inventoryDict=json.load(file)

def write_inventoryDictionary_to_JSON():
    try:
        with open(FILE_PATH_JSON,'+r') as file:
            file.write(json.dumps(inventoryDict,indent=4))
    except Exception as ex:
        logging.critical(ex)

def add_inventory(KEY):
    try:
        inventory=Inventory(input("Enter Name of {}\n".format(KEY)),float(input("Enter weight of {}\n".format(KEY))),float(input("Enter price per Kg\n")))
        inventoryDict.setdefault(KEY,[]).append(inventory.__dict__)
    except Exception as ex:
        logging.critical(ex)


def read_JSON_to_calculate_inventory_cost(KEY):
    try:
        totalInventoryWeight=0
        totalInventoryCost=0
        inventorylist=inventoryDict.get(KEY,"Not found")
        if(inventorylist=='Not found'):
            print(inventorylist)
        for inventory in inventorylist:
            inventoryName=inventory.get("name")
            inventoryWeight=inventory.get("weight")
            inventoryPricePerKg=inventory.get("pricePerKg")
            totalInventoryWeight+=inventoryWeight
            totalInventoryCost+=(inventoryWeight*inventoryPricePerKg)
            print("Name of Inventory {0} weight {1} perKg price {2} ".format(inventoryName,inventoryWeight,inventoryPricePerKg))
            print("Inventory Cost {0}  ".format(inventoryWeight*inventoryPricePerKg))
            print("================================================================")
        print("Name of Inventory {0} TotalWeight {1} TotalCost {2} ".format(KEY,totalInventoryWeight,totalInventoryCost))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except Exception as ex:
        logging.critical(ex)

def main():
    load_JSON_to_dictionary()
    choice=''
    while(choice!='5'):
        print("1.Update WHEAT inventory\n2.Update PULSES inventory\n3.Print Inventory cost of WHEAT\n4.Print Inventory cost of PULSES\n5.Quit Program")
        choice=input("Enter your choice")
        if(choice=='1'):
            print("You have choosen to Add new WHEAT inventory")
            add_inventory("WHEAT")
        elif(choice=='2'):
            print("You have choosen to Add new PULSES inventory")
            add_inventory("PULSES")
        elif(choice=='3'):
            print("You have choosen to Print Inventory Cost of WHEAT")
            read_JSON_to_calculate_inventory_cost("WHEAT")
        elif(choice=='4'):
            print("You have choosen to Calculate Inventory Cost of PULSES")
            read_JSON_to_calculate_inventory_cost("PULSES")
        elif(choice=='5'):
            print("Writing inventory to JSON file")
            write_inventoryDictionary_to_JSON()
            print("Exited From the program")

if __name__=="__main__":
    main()
