import logging
import os
from datetime import datetime #type:ignore


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
directory,filepath=os.path.split(os.path.join(os.getcwd(),"log",LOG_FILE))

os.makedirs(directory,exist_ok=True)
LOG_FILE_PATH=os.path.join(directory,filepath)

with open(LOG_FILE_PATH,"w") as op:
    pass

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
