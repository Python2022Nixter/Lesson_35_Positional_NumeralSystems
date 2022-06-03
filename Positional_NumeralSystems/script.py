"""
Index 
Radix (base)
Digits
Position
1125( decimal) = 5 * (10 ** 0) + 2 * (10 ** 1) + 1 * (10 ** 2) + 1 * (10 ** 3)  
    
Binary ( base 2)
0 1 
Octal ( base 8)
0 1 2 3 4 5 6 7
Decimal ( base 10)
0 1 2 3 4 5 6 7 8 9
Hexadecimal ( base 16)
0 1 2 3 4 5 6 7 8 9 A B C D E F
"""
# for n in range(100):
#     print(f"decimal: {n:8d} hex: {n:8x} oct: {n:8o} bin: {n:032b}")
#     pass

"""
decimal:        0 hex:        0 oct:        0 bin: 00000000000000000000000000000000
decimal:        1 hex:        1 oct:        1 bin: 00000000000000000000000000000001
decimal:        2 hex:        2 oct:        2 bin: 00000000000000000000000000000010
decimal:        3 hex:        3 oct:        3 bin: 00000000000000000000000000000011
decimal:        4 hex:        4 oct:        4 bin: 00000000000000000000000000000100
decimal:        5 hex:        5 oct:        5 bin: 00000000000000000000000000000101
decimal:        6 hex:        6 oct:        6 bin: 00000000000000000000000000000110
decimal:        7 hex:        7 oct:        7 bin: 00000000000000000000000000000111
decimal:        8 hex:        8 oct:       10 bin: 00000000000000000000000000001000
decimal:        9 hex:        9 oct:       11 bin: 00000000000000000000000000001001
decimal:       10 hex:        a oct:       12 bin: 00000000000000000000000000001010
decimal:       11 hex:        b oct:       13 bin: 00000000000000000000000000001011
decimal:       12 hex:        c oct:       14 bin: 00000000000000000000000000001100
decimal:       13 hex:        d oct:       15 bin: 00000000000000000000000000001101
"""

# Bitwise operations
"""
Operator    Exemple   Meaning
&           a & b      Bitwise AND
|           a | b      Bitwise OR
^           a ^ b      Bitwise XOR
~           ~a         Bitwise NOT
<<          a << n     Bitwise left shift
>>          a >> n     Bitwise right shift


Operator    Exemple   Meaning
&=          a &= b     a = a & b
|=          a |= b     a = a | b
^=          a ^= b     a = a ^ b
<<=         a <<= n    a = a << n
>>=         a >>= n    a = a >> n

Shift operators are used to move bits to the left or right.
a = 10101010
a << 2 = 1010101000
a >> 2 = 00101010

Truth table


 ip adress
 79.176.37.44
 1001111.10110000.0010010o1.00101100
 mask
 255.255.0.0
 11111111.11111111.00000000.00000000

"""

# ineteger literals
a = 10
b = 0b10  # binary
c = 0o10  # octal
d = 0x10  # hexadecimal
print(a, b, c, d)

a = 0b101  # binary 101 ~ 101  -> 1010 - 1 = 1001 -> 0110
print(F"{a:b} {~a:b}")
print(F"{a:d} {~a:d}")

# two's complement
"""
convert to two's complement
1. invert all bits
2. add 1

convert from two's complement
1. subtract 1
2. convert all bits
"""

a = 10
print(a)
print(a << 1)
print(a << 2)
print(a << 3)
print()
print(a >> 1)  # a / 2
print(a >> 2)  # a / 2 / 2
print(a >> 3)
print(a >> 4)
print(a >> 5)

# 10100011001110101110
"""
ряды в кинотеатре
0000000000000000
1111111111111111
1001110001001000
1111111000001111
"""

# set bit
# bits | (1 << bitN)
print(F"{0b11110000111100001:b}")
print(F"Set bit N 1")
print(F"{0b11110000111100001 | (1 << 1):b}")
# clear bit
print(F"Clear bit N 1")
print(F"{0b11110000111100001 & ~(1 << 1):b}")

# get bit
print(F"Get bit N 1")
print(F"{0b11110000111100001 & (1 << 1):b}")

print(F"Get bit N 0")
print(F"{0b11110000111100001 & (1 << 0):b}")

# toogle bit
print(F"Toogle bit N 3")
print(F"{0b11110000111100001 ^ (1 << 3):b}")