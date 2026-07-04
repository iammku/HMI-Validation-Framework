def test_speed(vehicle):
    expected_speed=120
    actual_speed=vehicle.speed
    assert actual_speed==expected_speed
def test_fuel(vehicle):
    expected_fuel=20
    actual_fuel=vehicle.fuel
    assert actual_fuel==expected_fuel
def test_door(vehicle):
    expected_door="CLOSED"
    actual_door=vehicle.door
    assert actual_door==expected_door
def test_battery(vehicle):
    expected_battery=30
    actual_battery=vehicle.battery
    assert actual_battery==expected_battery
def test_health_score(vehicle):
    expected_score=60
    actual_score=vehicle.calculate_health_score()
    assert actual_score==expected_score
def test_health_status(vehicle):
    actual_status=vehicle.health_status()
    expected_status="Warning"
    assert actual_status==expected_status
def test_warning_list(vehicle):
    expected_warnings=["Low fuel","Battery Low"]
    actual_warnings=vehicle.generate_warnings()
    assert actual_warnings==expected_warnings
def test_can_connection(can_connection):
    expected = "CONNECTED"
    actual = can_connection
    assert actual == expected