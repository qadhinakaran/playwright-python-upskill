import pytest


@pytest.fixture(scope = "function")
def PreSetupWork():
    print("I setup System")

# scope = function & scope = module
# module -> Once per session