import logging

logger = logging.getLogger("framework")
logger.setLevel(logging.WARNING)
logging.basicConfig(format= "%(asctime)s||%(name)s||%(message)s||%(levelname)s",
                    level=logging.DEBUG)

logger.debug("A")
logger.info("B")
logger.warning("C")
logger.error("D")
logger.critical("E")