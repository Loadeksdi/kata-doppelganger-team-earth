import pytest
from calculator import Calculator
class NotAuthorizedError(Exception):
    pass

class Authorizer:
    def authorize(self):
        return False

def test_divide_should_raise_error_when_not_authorized():
    # TODO: write a test that fails due to the bug in
    # Calculator.divide
    with pytest.raises(NotAuthorizedError, match= "Not authorized"):
        num= 1
        denom= 2
        calculator= Calculator(Authorizer())
        calculator.divide(numerator= num, denominator= denom)
        
