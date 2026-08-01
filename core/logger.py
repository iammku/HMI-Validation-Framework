import logging
from core.paths import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)
log_file=LOG_DIR/"framework.log"

logger= logging.getLogger("framework")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter= logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler= logging.StreamHandler()
    file_handler=logging.FileHandler(
        log_file,
        encoding="utf-8"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)