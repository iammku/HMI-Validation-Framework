import pytest
from vehicle import Vehicle
@pytest.fixture(scope="session")
def can_connection():
    print("Opening CANoe...")
    yield
    print("Closing CANoe..")
@pytest.fixture(scope="module")
def logger(can_connection):
    print("Logger started")
    yield
    print("Logger Closed")
@pytest.fixture()
def vehicle(logger):
    print("Vehicle Boot")
    vehicle_obj=Vehicle(
        speed=120,
        fuel=20,
        battery=30,
        door="CLOSED",
        seatbelt="BUCKLED",
        ignition="ON"
    )
    yield vehicle_obj
    print("Vehicle Shutdown")
@pytest.fixture()
def expected_vehicle():
    return {
    "speed":120,
    "fuel":20,
    "battery":30,
    "door":"CLOSED",
    "seatbelt":"BUCKLED",
    "ignition":"ON"
}
@pytest.fixture()
def vehicle_theme():
    return{
        "Theme": "Blue",
    }