import pytest
import sys
@pytest.fixture(autouse=True)
def common_setup():
    print("Setup")
    yield
    print("Closed")
def test_one():
    print("Pass")
def test_two():
    print("Fail")
def test_three():
    print("Retest")

def display_speed():
    print("speed=120")
def test_speed(capsys):
    display_speed()
    captured=capsys.readouterr()
    assert captured.out=="speed=120\n"
def cluster_boot():
    print("Cluster booted successfully")
def test_cluster_boot(capsys):
    cluster_boot()
    text=capsys.readouterr()
    assert "Cluster booted successfully\n" in text