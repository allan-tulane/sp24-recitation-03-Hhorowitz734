"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):

    #print("x:", x.decimal_val)
    #print("y:", y.decimal_val)
    #print()
    #Pad x and y
    xvec, yvec = pad(x.binary_vec, y.binary_vec)
    
    #x = binary2int(xvec) #unnecessary
    #y = binary2int(yvec)
    
    # Base Case -> The lengths of the vectors <= 1 
    if len(xvec) <= 1 or len(yvec) <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
    #Helper variables for length
    n = len(xvec)
    m = n // 2
    
    #Split
    x_left, x_right = split_number(x.binary_vec)
    y_left, y_right = split_number(y.binary_vec)
    
    #I was having errors before adding this line confirming none of the halves = 0
    if x_left.decimal_val == 0 or x_right.decimal_val == 0 or y_left.decimal_val == 0 or y_right.decimal_val == 0:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
    #Recursive calls 
    P1 = _quadratic_multiply(x_left, y_left)
    P2 = _quadratic_multiply(x_right, y_right)
    P3 = _quadratic_multiply(BinaryNumber(x_left.decimal_val + x_right.decimal_val), 
                             BinaryNumber(y_left.decimal_val + y_right.decimal_val))
    
    #Derived directly from the karatsuba equation
    result = bit_shift(P1, 2*m).decimal_val + bit_shift(BinaryNumber(P3.decimal_val - P1.decimal_val - P2.decimal_val), m).decimal_val + P2.decimal_val

    return BinaryNumber(result)


    

def xtest_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f

    f(x, y)
    
    return (time.time() - start)*1000

    
    


#print(quadratic_multiply(BinaryNumber(2), BinaryNumber(8)))