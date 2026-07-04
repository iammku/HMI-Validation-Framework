import pytest
@pytest.fixture
def can():
    print("\nConnected")
    yield
    print("Disconnected")
@pytest.fixture()
def lamp():
    print("On")
    yield
    print("\nOff")
def test_light(can,lamp):
    print("Done")
