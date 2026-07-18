import pytest
from vehicle import Vehicle
# @pytest.fixture
# def vehicle1():
#     return Vehicle(120, 20, "BUCKLED", "OPEN", "ON")
@pytest.fixture
def vehicle1():
    return Vehicle(
        speed=120,
        fuel=20,
        door="OPEN",
        ignition="ON",
        seatbelt="BUCKLED",
    )
@pytest.fixture
def vehicle_status():
    return {
    "health":"Healthy",
    "warning":"None"
}
@pytest.fixture
def warning_list():
    return [
    "Low Fuel",
    "Door Ajar"
]
@pytest.fixture
def cluster(vehicle1):
 return {
    "speed": vehicle1.speed,
    "fuel": vehicle1.fuel,
    "status": "ACTIVE"
}