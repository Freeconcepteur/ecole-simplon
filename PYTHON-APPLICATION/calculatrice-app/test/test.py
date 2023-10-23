mymodule = None
try:
    from components import mymodule
except ImportError:
    pass

# test functions of "mymodule"
from components.mymodule import addition , multiplication, soustraction, division
class Test_Mymodule():

    def test_add(self):
        assert addition(5,2) == 7, "addition is looking not ok"
    
    def test_sous(self):
        assert soustraction(5,2) == 3, "soustraction is looking not ok"

    def test_mul(self):
        assert multiplication(5,2) == 10, "multiplication is looking not ok"
    
    def test_div(self):
        assert division(10,2) == 5, "division is looking not ok"
