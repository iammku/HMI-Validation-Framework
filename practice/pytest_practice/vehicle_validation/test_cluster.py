def test_one(vehicle):
    expected_speed=120
    assert vehicle.speed==expected_speed
def test_two(vehicle):
    expected_fuel=20
    assert vehicle.fuel==expected_fuel
def test_three(vehicle):
    expected_status="CLOSED"
    assert vehicle.door==expected_status
def test_four(vehicle):
    expected_ign="ON"
    assert vehicle.ignition==expected_ign
def test_five(vehicle):
    expected_seat="BUCKLED"
    assert vehicle.seatbelt==expected_seat
def test_six(vehicle):
    expected_health="Warning"
    assert vehicle.calculate_health()==expected_health
def test_seven(vehicle):
    expected_vehicle_status="Vehicle Ready"
    assert vehicle.get_vehicle_status()==expected_vehicle_status
def test_eight(can_connection):
    expected="CONNECTED"
    assert can_connection==expected