import pytest


@pytest.fixture
def say_hello():
    print('\nHello!')
    yield print('Testing')
    print('\nBye!')
