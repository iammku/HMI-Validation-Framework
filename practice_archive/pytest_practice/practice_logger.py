import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("This is example")

logging.basicConfig(filename="log.txt",
                    filemode="a",
                    level=logging.ERROR,
                    #current_time, log_level, message
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("This is information")
logging.debug("DEV attention required")
logging.warning("Low fuel")
logging.error("No file present")
logging.critical("cluster crashed")