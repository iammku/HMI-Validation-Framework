import pytest
from vehicle import Vehicle
@pytest.mark.parametrize(
    "vehicle_obj, expected",
    [
        (Vehicle(80,80,"CLOSED"),"Healthy"),
        (Vehicle(120,20,"CLOSED"),"Warning"),
        (Vehicle(150,10,"OPEN"),"Critical"),
        (Vehicle(60,15,"OPEN"),"Critical"),
        (Vehicle(90,60,"CLOSED"),"Healthy")
    ],
    ids=["City Driving",
        "Low Fuel",
        "Door Open",
        "Critical State",
        "Normal Drive"]
)
def test_vehicle1(vehicle_obj,expected):
    actual=vehicle_obj.health_status()
    assert actual==expected