import pytest
from vehicle import Vehicle
@pytest.mark.parametrize("speed, fuel, door, expected",
                        [(80,80,"CLOSED","Healthy"),
                        (120,20,"CLOSED","Warning"),
                        (150,10,"OPEN","Critical"),
                        (60,15,"OPEN","Critical"),
                        (90,60,"CLOSED","Healthy")],
ids=["City Driving","Low Fuel","Door Open","Critical State","Normal Drive"]
                         )
def test_vehicle(speed, fuel, door, expected):
    vehicle_obj=Vehicle(speed=speed,fuel=fuel,door=door)
    assert vehicle_obj.health_status()==expected