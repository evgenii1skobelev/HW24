import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_adding_success(self):
        assert self.calc.adding( self,5, 4) == 9
    def test_multiply_success(self):
        assert self.calc.multiply(self,3,2) == 6
    def test_division_success(self):
        assert self.calc.division(self,6,2) == 3
    def test_subtraction_success(self):
        assert self.calc.subtraction(self,8,4) == 4
    def test_adding_unsuccess(self):
        assert self.calc.adding(self,4,2) == 5
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,3,0)
    def teardown(self):
        print('Выполнение метода Teardown')