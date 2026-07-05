import pytest
from vehicle import Vehicle
def test_vehicle_data(vehicle,expected_vehicle):
    assert vehicle.speed==expected_vehicle["speed"]
    assert vehicle.fuel==expected_vehicle["fuel"]
    assert vehicle.door==expected_vehicle["door"]
    assert vehicle.ignition==expected_vehicle["ignition"]
    assert vehicle.battery==expected_vehicle["battery"]
    assert vehicle.seatbelt==expected_vehicle["seatbelt"]

@pytest.mark.parametrize(
    "speed, expected",
    [
        (80, False),
        (100, False),
        (120, False),
        (130, True),
        (150, True)
     ],
)
def test_overspeed(speed, expected):
    vehicle_obj=Vehicle(
        speed=speed,
        fuel=20,
        battery=30,
        door="CLOSED",
        seatbelt="BUCKLED",
        ignition="ON"
    )
    actual=vehicle_obj.is_overspeed()
    assert actual==expected

@pytest.mark.parametrize(
"fuel, battery, door, seatbelt, ignition, expected",
    [(80,80, "CLOSED", "BUCKLED", "ON", "Healthy"),
    (19,80, "CLOSED", "BUCKLED", "OFF", "Warning"),
    (10,10, "OPEN", "UNBUCKLED", "OFF", "Critical"),
    (60,20, "CLOSED", "UNBUCKLED", "ON", "Warning"),
     ],
    ids=["Healthy Vehicle",
        "Low Fuel",
        "Critical Vehicle",
        "Battery Low"]
)
def test_health(fuel, battery, door, seatbelt, ignition, expected):
    vehicle_obj=Vehicle(
        speed=100,
        fuel=fuel,
        battery=battery,
        door=door,
        seatbelt=seatbelt,
        ignition=ignition
    )
    actual= vehicle_obj.health_status()
    assert actual==expected
def test_warning_list(vehicle):
    actual=vehicle.generate_warnings()
    expected=[
        "Battery Low",
        "Low Fuel"
    ]
    assert actual==expected