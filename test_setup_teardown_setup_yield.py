import pytest

@pytest.fixture(scope="function")
def setup_and_teardown():
    print("\n___start_________This is browser setup with url and it is running before each tests")
    yield
    print("\n___end_____This is teardown setup means to close after running each test function")


def test_first_test(setup_and_teardown):
    print("I am running first test case")

def test_second_test(setup_and_teardown):
    print("I am running second test case")