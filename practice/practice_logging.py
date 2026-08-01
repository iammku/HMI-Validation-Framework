import logging
from logging import critical

logging.basicConfig(level=logging.INFO,
                    format="%(message)s- %(asctime)s- %(name)s- %(levelname)s",
                    )
logger =logging.getLogger(__name__)

logger.debug("Debug Message")
logger.info("Framework Started")
logger.warning("Optional Config missing")
logger.error("Unable to connect to CAN")
logger.critical("Framework crashes")
