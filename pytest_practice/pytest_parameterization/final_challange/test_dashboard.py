def test_theme(vehicle, vehicle_theme):
    actual="Blue"
    assert actual==vehicle_theme["Theme"]

def test_cluster_ready(vehicle):
    expected = "Warning"
    actual = vehicle.health_status()
    assert actual == expected
def test_warning_popup(vehicle):
    expected = [
        "Battery Low",
        "Low Fuel"
    ]
    actual = vehicle.generate_warnings()
    assert actual == expected