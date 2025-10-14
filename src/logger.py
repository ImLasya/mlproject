# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
# logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)


# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# if __name__ == "__main__":
#     logging.info("Logging has started")


import logging
import os
from datetime import datetime

# Step 1: Create a logs folder
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Step 2: Define log file name and full path
LOG_FILE = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 3: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Step 4: Test it
if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file created at: {LOG_FILE_PATH}")
