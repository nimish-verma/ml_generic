import logging
import os
from datetime import datetime
# from src.logger import loggin

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] [ %(levelname)s ] [ %(filename)s ] [ %(funcName)s ] [ %(lineno)d ] [ %(message)s ]",
    level = logging.INFO
)


# if __name__ == "__main__":
    
    
    
#     logging.info("logging has started")