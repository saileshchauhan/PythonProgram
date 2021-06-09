#Importing From LogConfig logging config
import logconfig
import logging

try:
    raise ValueError("Testing configuartion For log config")
except Exception as ex:
    logging.critical(ex)




