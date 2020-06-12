import pytest
from test_pytesthomework.test_cal import Calculator

@pytest.fixture()
def reckon():
    cal=Calculator()
    print("开始计算")
    yield cal
    print("计算结束")

