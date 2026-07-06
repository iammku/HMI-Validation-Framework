import sys
import pytest
from vehicle import Vehicle
@pytest.fixture()
def vehicle():
    print("Vehicle is Ready")
    vehicle_obj=Vehicle()
    yield vehicle_obj
    print("Vehicle Closed")
@pytest.mark.smoke
def test_boot(vehicle):
    actual=vehicle.boot_cluster()
    expected="Booted"
    assert actual==expected
@pytest.mark.skip(reason="Bluetooth feature not ready")
def test_bluetooth(vehicle):
    actual=vehicle.bluetooth()
    expected="Connected"
    assert actual==expected
@pytest.mark.skipif(
    sys.platform=="darwin",
    reason="Camera not supported on mac"
)
def test_camera(vehicle):
    actual=vehicle.camera()
    assert actual is False
@pytest.mark.xfail(reason="Known issue")
def test_navigation(vehicle):
    actual=vehicle.navigation()
    expected="Turn Right"
    assert actual==expected
@pytest.mark.regression
def test_adas(vehicle):
    actual=vehicle.adas()
    expected="Hands-on"
    assert actual==expected
@pytest.mark.xfail(reason="AOS-12345")
def test_cluster(vehicle):
    actual=vehicle.cluster()
    expected="Blank"
    assert actual==expected
@pytest.mark.sanity
@pytest.mark.smoke
@pytest.mark.skipif(sys.platform=="win32",
                  reason="Not supported on windows",)
def test_IVI(vehicle):
    actual=vehicle.IVI()
    expected="Ready"
    assert actual==expected