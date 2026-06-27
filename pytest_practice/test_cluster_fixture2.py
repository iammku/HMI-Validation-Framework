import pytest
@pytest.fixture
def ignition():
    return "ON"
@pytest.fixture
def can_connection():
    return "enabled"
@pytest.fixture
def vehicle_speed():
    return 120
def test_cluster(ignition, can_connection, vehicle_speed):
    expected_ignition="ON"
    expected_can_connection="enabled"
    expected_vehicle_speed=120
    assert ignition==expected_ignition
    assert can_connection==expected_can_connection
    assert vehicle_speed==expected_vehicle_speed
@pytest.fixture
def vehicle_data():
    return {
        "speed": 120,
        "fuel": 15,
        "ignition": "ON",
        "seatbelt": "Buckled",
        "door": "Closed",
    }
def test_vehicle_data(vehicle_data):
    expected_speed=120
    expected_fuel=15
    expected_ignition="ON"
    expected_seatbelt="Buckled"
    expected_door="Closed"
    assert vehicle_data["speed"]==expected_speed
    assert vehicle_data["fuel"]==expected_fuel
    assert vehicle_data["ignition"]==expected_ignition
    assert vehicle_data["door"]==expected_door
    assert vehicle_data["seatbelt"]==expected_seatbelt
@pytest.fixture
def fuel():
    print("Fixture")
    return 15
def test_one(fuel):
    print("One")
def test_two(fuel):
    print("two")
#2 times
class Vehicle1:
    def __init__(self, speed, fuel, door):
        self.speed=speed
        self.fuel=fuel
        self.door=door
@pytest.fixture
def car():
    return Vehicle1(120,15,"Open")
def test_car(car):
    assert car.speed==120
    assert car.fuel==15
    assert car.door=="Open"
@pytest.fixture
def speed():
    return 120
@pytest.fixture
def vehicle(speed):
    return {
        "speed":speed
    }
def test_vehicle_speed(vehicle):
    expected_speed=120
    assert vehicle["speed"]==expected_speed

@pytest.fixture
def speed():
    print("Speed")
    return 120
@pytest.fixture
def fuel():
    print("Fuel")
    return 15
@pytest.fixture
def vehicle_t(speed, fuel):
    print("Vehicle")
    return {
        "speed":speed,
        "fuel": fuel
    }
def test_cluster1(vehicle_t):
    print("cluster_test")
def test_dashboard(speed):
    print("Dashboard Test")