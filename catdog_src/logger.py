import logging
import os
from datetime import datetime

"""
Logging for the project

"""
# Creating instance for log w.r.t time
LOG_FILE_NAME=f"{datetime.now().strftime('%d%m%Y__%H%M%S')}.log"

#creating directory
LOG_FILE_DIR=os.path.join(os.getcwd(),'logs')

#if not exist creating one

os.makedirs(LOG_FILE_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s %(message)s",
    level=logging.INFO,
)
