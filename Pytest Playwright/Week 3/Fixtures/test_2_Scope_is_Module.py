import pytest


@pytest.fixture(scope = "module")
def prework():
    print("I Setup browser Instance")

def test_first(prework):
    print("This is the first check")

def test_second(prework):
    print("This is the second check")

def test_third(PreSetupWork):
    print("This is the third check")

