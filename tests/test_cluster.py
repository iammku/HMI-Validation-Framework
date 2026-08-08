import pytest
from core.cluster import VehicleStateError

def test_vehicle(framework_logger, cluster):
    framework_logger.info("Running vehicle test")
    assert cluster.get_vehicle() == "Mustang"
    # cluster.show_cluster_info()
    # print(cluster.is_speeding())
    # print(cluster.is_dark_theme())
    # print(cluster.can_vehicle_move())
def test_speed(cluster):
    assert cluster.get_speed() == 120
    assert cluster.is_speeding() == True
def test_gear(cluster):
    assert cluster.get_gear() == "Park"
def test_theme(cluster):
    expected_theme= "dark"
    assert cluster.get_theme().lower() == expected_theme
    assert cluster.is_dark_theme() is True
def test_speeding(cluster):
    assert cluster.is_speeding() == True
def test_vehicle_move(cluster):
    assert cluster.can_vehicle_move() == False
def test_warning(cluster):
    assert cluster.warning1.is_seatbelt_warning_active()==True
def test_accelerate_without_ignition(cluster):
    with pytest.raises(VehicleStateError):
        cluster.accelerate(20)
def test_invalid_gear(cluster):
    with pytest.raises(ValueError):
        cluster.shift_gear("xyz")
def test_engine_start(cluster):
    cluster.start_engine()
    assert cluster.is_ignition_on()
def test_accelerate(cluster):
    cluster.start_engine()
    cluster.shift_gear("D")
    cluster.accelerate(20)
    assert cluster.get_speed() == 140
def test_brake(cluster):
    cluster.start_engine()
    cluster.shift_gear("D")
    cluster.accelerate(40)
    cluster.brake(10)

    assert cluster.get_speed() == 150
def test_seatbelt_warning_off(cluster):
    cluster.start_engine()
    cluster.shift_gear("D")
    cluster.accelerate(20)
    cluster.fasten_seatbelt()

    assert not cluster.warning1.is_seatbelt_warning_active()

def test_stop_engine_while_moving(cluster):
    cluster.start_engine()
    cluster.shift_gear("D")
    cluster.accelerate(20)

    with pytest.raises(VehicleStateError):
        cluster.stop_engine()