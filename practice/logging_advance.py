import logging
from pathlib import Path

project_root= Path(__file__).parent.parent
print(project_root)
log_path= project_root/ "logs"
log_path.mkdir(exist_ok=True)
log_file= log_path/ "framework.log"

#create logger
logger=logging.getLogger("framework")
logger.setLevel(logging.INFO)

#configure logger
if not logger.handlers:
    formatter=logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler=logging.StreamHandler()
    file_handler=logging.FileHandler(
        log_file,
        encoding="utf-8"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

#logging
logger.info("Configuration Loaded")
logger.warning("Bluetooth Disconnected")
logger.error("CAN Timeout")
logger.critical("Framework Initialization Failed")