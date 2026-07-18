import pytest
@pytest.fixture
def speed():
    return 120
def test_speed(speed):
    assert speed==120
@pytest.fixture
def fuel():
    return 15
def test_fuel(fuel):
    assert fuel==20
@pytest.fixture
def door():
    return "OPEN"
def test_door(door):
    assert door=="OPEN"
@pytest.fixture
def vehicle_health():
    return "Healthy"
def test_vehicle_health(vehicle_health):
    assert vehicle_health=="Healthy"
@pytest.fixture
def vehicle_data():
    return {
        "speed":120,
        "fuel":15,
        "door":"OPEN"
    }
def test_vehicle_data(vehicle_data):
    assert vehicle_data=={
        "speed":120,
        "fuel":15,
        "door":"OPEN"
    }