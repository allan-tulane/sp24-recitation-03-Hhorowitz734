from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(5)) == 4*5
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(2)) == 8*2
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(5)) == 0*5
    assert quadratic_multiply(BinaryNumber(9), BinaryNumber(2)) == 9*2
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(16)) == 4*16


    