
from main.inu import add,subtract,multiply,divide

def test_add():
    assert add(2, 5) == 7

def test_subtract():
    assert subtract(50, 13) == 37

def test_multiply():
    assert multiply(5, 2) == 10

def test_divide():
     assert divide(4, 2) == 2
