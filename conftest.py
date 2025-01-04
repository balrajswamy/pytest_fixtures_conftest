import pytest

@pytest.fixture(scope="session") # it runs only once before running all the test
def preWork():
    print("\n_______________I setup browser instance from the Global level__________\n")

