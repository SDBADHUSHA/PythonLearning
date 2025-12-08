# Interger Datatype is used to store whole numbers without decimal places
# Interger Datatype is immutable
print(dir(int)) #prints all the methods that can be used with integer
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
# '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
# '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
# '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
# '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__',
# '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

#   Example of all integer functions are given below    
number1 = 10
# Correct usage of integer methods and properties

# 1. Standard arithmetic (uses dunder methods internally)
print(abs(number1))          # __abs__: 10
print(number1 + 10)          # __add__: 20
print(bool(number1))         # __bool__: True
import math
print(math.ceil(number1))    # __ceil__: 10
print(number1.__class__)     # __class__: <class 'int'>

# 2. Comparison (uses dunder methods internally)
print(number1 == 10)         # __eq__: True
print(number1 >= 5)          # __ge__: True
print(number1 > 5)           # __gt__: True
print(number1 <= 20)         # __le__: True
print(number1 < 20)          # __lt__: True
print(number1 != 5)          # __ne__: True

# 3. Type Conversion
print(float(number1))        # __float__: 10.0
print(int(number1))          # __int__: 10
print(str(number1))          # __str__: '10'
print(repr(number1))         # __repr__: '10'

# 4. Bitwise Operations
print(number1 & 1)           # __and__: 0
print(number1 | 1)           # __or__: 11
print(number1 ^ 1)           # __xor__: 11
print(~number1)              # __invert__: -11
print(number1 << 1)          # __lshift__: 20
print(number1 >> 1)          # __rshift__: 5

# 5. Math Operations
print(divmod(number1, 3))    # __divmod__: (3, 1)
print(number1 % 3)           # __mod__: 1
print(number1 * 2)           # __mul__: 20
print(-number1)              # __neg__: -10
print(+number1)              # __pos__: 10
print(pow(number1, 2))       # __pow__: 100
print(round(number1))        # __round__: 10
print(number1 - 5)           # __sub__: 5
print(number1 / 2)           # __truediv__: 5.0
print(number1 // 3)          # __floordiv__: 3

# 6. Public Integer Methods (Valid to call directly)
print(number1.bit_count())       # Number of ones in binary representation
print(number1.bit_length())      # Number of bits necessary to represent the number
print(number1.as_integer_ratio()) # Returns (numerator, denominator) pair
print(number1.to_bytes(2, 'big')) # Return the integer as a bytes object

# 7. Class Methods (Call on int class)
print(int.from_bytes(b'\x00\x0a', 'big')) # Return the integer represented by the given array of bytes

# 8. Properties (No parentheses)
print(number1.real)          # The real part of the complex number
print(number1.imag)          # The imaginary part of the complex number
print(number1.numerator)     # The numerator of a rational number in lowest terms
print(number1.denominator)   # The denominator of a rational number in lowest terms

# Example 2, alternatively all the functions of int can be used as interger value example 10
print(abs(10))
print(bool(10))
print(float(10))
print(int(10))
print(str(10))
print(repr(10))

# 2. Comparison (uses dunder methods internally)
print(10 == 10)         # __eq__: True
print(10 >= 5)          # __ge__: True
print(10 > 5)           # __gt__: True
print(10 <= 20)         # __le__: True
print(10 < 20)          # __lt__: True
print(10 != 5)          # __ne__: True

# 4. Bitwise Operations
print(10 & 1)           # __and__: 0
print(10 | 1)           # __or__: 11
print(10 ^ 1)           # __xor__: 11
print(~10)              # __invert__: -11
print(10 << 1)          # __lshift__: 20
print(10 >> 1)          # __rshift__: 5

# 5. Math Operations
print(divmod(10, 3))    # __divmod__: (3, 1)
print(10 % 3)           # __mod__: 1
print(10 * 2)           # __mul__: 20
print(-10)              # __neg__: -10
print(+10)              # __pos__: 10
print(pow(10, 2))       # __pow__: 100
print(round(10))        # __round__: 10
print(10 - 5)           # __sub__: 5
print(10 / 2)           # __truediv__: 5.0
print(10 // 3)          # __floordiv__: 3





# 
