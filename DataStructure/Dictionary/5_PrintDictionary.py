'''
@Author:Sailesh Chauhan
@Date:2021-06-12
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-12
@Title: Print Dictionary in Table format.
'''

#Importing logConfig for error logging
import logconfig
import logging


dictionary={}

dictionary = {1: ["Sandra", 24, 'Data Engineer'],2: ["Richie", 20, 'Google Cloud'],3: ["Lauren", 21, 'Amazon Web Services'],
        }
  
print ("{:^10} {:^10} {:^10} {:^10}".format('ID','NAME', 'AGE', 'COURSE'))
  
for key, value in dictionary.items():
    id=key
    name, age, course = value
    print ("{:^10} {:^10} {:^10} {:^10}".format(id,name, age, course))