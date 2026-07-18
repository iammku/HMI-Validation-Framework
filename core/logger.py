import logging
logging.basicConfig(
    level=logging.INFO,
    filename="framework.log",
    filemode="w",
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger1=logging.getLogger()
