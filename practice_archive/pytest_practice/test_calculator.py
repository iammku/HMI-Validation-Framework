import pytest
@pytest.mark.parametrize("speed", [80,100,120,140])
def test_speed(speed):
    assert speed<=120

@pytest.mark.parametrize("fuel",[20,50,69])
def test_fuel(fuel):
    assert fuel>=20

@pytest.mark.parametrize("speed, fuel",[(120,20),(100,30),(80,40)])
def test_vehicle(speed, fuel):
    assert fuel>=20
    assert speed<=120

@pytest.mark.parametrize("speed, expected",
                         [(100, True),
                          (120, True),
                          (150, False)]
                         )
def test_vehicle1(speed, expected):
    assert (speed<=120)==expected