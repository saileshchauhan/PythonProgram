'''
@Author:Sailesh Chauhan
@Date:2021-06-06
@Last Modified by:Sailesh Chauhan
@Last Modified time:2021-06-06
@Title:Clinic Management Application
'''

import json
import logging
from decouple import config

FILE_PATH_LOG=config('log_File_Path')
FILE_PATH_JSON=config('JSON_File_Path')

logging.basicConfig(filename=FILE_PATH_LOG,level=logging.CRITICAL,format='%(asctime)s - %(levelname)s - %(message)s')


