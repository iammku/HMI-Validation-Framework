from core.logger import logger1
def test_cluster_logging():
    logger1.info("INFO logger")
    logger1.warning("Low Fuel")
    logger1.error("cluster crash")
    logger1.debug("This is test")
    logger1.critical("Test")
    assert True