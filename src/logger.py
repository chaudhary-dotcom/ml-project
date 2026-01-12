import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), 'logs')
# ensure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure root logger to write to the file (force replaces any previous basicConfig)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    force=True
)

# Add a console handler so logs also appear in the terminal
if not any(isinstance(h, logging.StreamHandler) for h in logging.getLogger().handlers):
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'))
    console_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(console_handler)

# Expose the configured logging module for imports like `from src.logger import logging`
logger = logging.getLogger(__name__)


