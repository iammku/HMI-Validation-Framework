import pytest
@pytest.fixture(autouse=True)
def environment():
    print("\nEnvironment Setup")
    yield
    print("\nEnvironment Cleanup")
