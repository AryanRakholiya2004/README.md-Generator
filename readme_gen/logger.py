import logging
import os
from datetime import datetime



LOG_DIR = datetime.now().strftime('%m_%d_%Y')  # Directory named with current date
log_path = os.path.join(os.getcwd(), 'logs', LOG_DIR)
os.makedirs(log_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%H_%M_%S')}.log"  # Log file named with current time
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] [ %(levelname)s ] %(name)s - %(lineno)s : %(message)s",
    level=logging.INFO,
)