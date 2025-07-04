import pytest


@pytest.fixture(scope = "function")
def firstWork():
    print("I Setup browser Instance")
    return "Pass"

@pytest.fixture(scope = "module")
def secondWork():
    print("I Setup Module Instance")
    yield
    print("Closed Browser")


def test_firstCheck(PreSetupWork, firstWork, secondWork):
    print("This is the first check")
    assert firstWork == "Pass"

def test_secondCheck(secondWork):
    print("This is the second check")
# Closef