import pytest
from pythoncode.cal import Calculator
import yaml

def pydakai():
    with yaml.safe_load(open("./data.yml")) as f:
        data=yaml.safe_load(f)
        return data
@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yml")))
class TestCal:
    @pytest.mark.add
    def test_add(self,reckon,a,b):
        print("加法",a,"+",b)
        assert a + b==reckon.add(a,b)

    def test_sub(self,reckon,a,b):
        print("减法",a,"-",b)
        assert a - b==reckon.sub(a,b)

    def test_mul(self,reckon,a,b):
        print("乘法",a,"*",b)
        assert a * b==reckon.mul(a,b)

    def test_div(self,reckon,a,b):
        print("除法",a,"/",b)
        assert a / b==reckon.div(a,b)