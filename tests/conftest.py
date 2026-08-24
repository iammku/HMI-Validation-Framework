import pytest
from core.logger import logger
from core.config_reader import get_config
from core.cluster import Cluster
from core.vehicle_simulator import VehicleSimulator
from core.event_dispatcher import EventDispatcher

@pytest.fixture(scope="session")
def config():
    logger.info("Initializing PyTest framework")
    """Return framework configuration"""
    cfg= get_config()
    logger.info(
        f"Framework initialize for Vehicle: {cfg["vehicle"]}"
    )
    return cfg
@pytest.fixture(scope="session")
def framework_logger():
    """shared framework logger"""
    return logger

@pytest.fixture(scope="function")
def cluster(config):
    #c1=Cluster(config)
    #return c1, can do this as well
    return Cluster(config)

@pytest.fixture(scope="function")
def dispatcher(cluster):
    return EventDispatcher(cluster)

@pytest.fixture(scope="function")
def simulator(cluster, dispatcher):
    c2= VehicleSimulator(cluster, dispatcher)
    return c2