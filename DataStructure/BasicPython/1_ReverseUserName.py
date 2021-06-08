'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title:Reverse user firstName and LastName.
'''

def reverse_username_lastname(userfirstName,userLastName):
    '''
    '''
    try:
        return [userfirstName[::-1],userLastName[::-1]]
    except Exception as ex:
        print(ex)

