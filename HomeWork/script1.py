# decimal - 10 
# octal - 12
# hex - A
# binary - 1010

print(bin(10)) # 0b1010
print(oct(10)) # 0o12
print(hex(10)) # 0xa

print(int("0b1010", 2)) # 10
print(int("0o12", 8)) # 10
print(int("0xa", 16)) # 10

test = bin(10)
print(test[2:]) # 1010