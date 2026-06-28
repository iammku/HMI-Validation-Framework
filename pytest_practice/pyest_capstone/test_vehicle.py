import pytest
def test_vehicle_speed(vehicle1):
    expected_speed=120
    assert vehicle1.speed==expected_speed
def test_fuel(vehicle1):
    expected_fuel=20
    assert vehicle1.fuel==expected_fuel
def test_door(vehicle1):
    expected_door="OPEN"
    assert vehicle1.door==expected_door
def test_ignition(vehicle1):
    expected_ignition="ON"
    assert vehicle1.ignition == expected_ignition
def test_seatbelt(vehicle1):
    expected_seatbelt="BUCKLED"
    assert vehicle1.seatbelt == expected_seatbelt
def test_calculate_health(vehicle1):
    expected_status="Warning"
    assert vehicle1.calculate_health()==expected_status
def test_warning(warning_list):
    assert "Low Fuel" in warning_list
def test_cluster(cluster):
    expected_speed=120
    expected_fuel=20
    expected_status="ACTIVE"
    assert cluster["speed"]==expected_speed
    assert cluster["fuel"]==expected_fuel
    assert cluster["status"]==expected_status
def test_vehicle_status(vehicle_status):
    assert vehicle_status["health"] == "Healthy"
    assert vehicle_status["warning"] == "None"