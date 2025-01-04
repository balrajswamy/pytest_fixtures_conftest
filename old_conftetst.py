import pytest

@pytest.fixture(scope="function")
def preWork():
    print("I setup browser instance from the Global level")

