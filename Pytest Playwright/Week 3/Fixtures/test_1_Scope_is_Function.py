import pytest


@pytest.fixture(scope = "function")
def preWork():
    print("I Setup browser Instance")

def test_firstCheck(preWork):
    print("This is the first check")

def test_secondCheck(preWork):
    print("This is the second check")
