'''
@Author:Sailesh Chauhan
@Date:2021-06-08
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-08
@Title: Print Date time using Datetime module
'''

import time,datetime
import logging
from decouple import config

FILE_NAME=config('Log_File_Path')
logging.basicConfig(filename=FILE_NAME,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')

print(time.strftime("%I:%M:%S"))
dateAndTime=datetime.datetime.now()
print(dateAndTime.strftime("%Y-%m-%d %H:%M:%S"))