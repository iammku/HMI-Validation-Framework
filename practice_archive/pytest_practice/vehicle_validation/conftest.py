import pytest
from vehicle import Vehicle
@pytest.fixture()
def vehicle(logger):
    print("Vehicle Initialization Started")
    vehicle=Vehicle(
    speed=120,
    fuel=20,
    door="CLOSED",
    ignition="ON",
    seatbelt="BUCKLED"
)
    vehicle.get_vehicle_status()
    vehicle.calculate_health()
    yield vehicle
    print("Vehicle Shutdown Completed")

@pytest.fixture(scope="session")
def can_connection():
    print("Opening CANoe...")
    yield "CONNECTED"
    print("Closing CAN")

@pytest.fixture(scope="module")
def logger():
    print("Logger started")
    yield
    print("Logger Closed")