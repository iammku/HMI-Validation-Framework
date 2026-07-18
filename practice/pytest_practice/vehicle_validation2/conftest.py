import pytest
from vehicle import Vehicle
@pytest.fixture()
def vehicle(logger):
    print("Vehicle Booting...")
    vehicle=Vehicle(
    speed=120,
    fuel=20,
    door="CLOSED",
    seatbelt="BUCKLED",
    ignition="ON",
    battery=30
)
    yield vehicle
    print("Vehicle Shutdown")
@pytest.fixture(scope="session")
def can_connection():
    print("Opening CANoe")
    yield "CONNECTED"
    print("Closing CANoe")
@pytest.fixture(scope="module")
def logger(can_connection   ):
    print("Logger started")
    yield
    print("Logger Closed")