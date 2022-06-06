a = 0b1000000000000000

for i in range(16):
    a |= 1 << i
    print(f"{a:b}")
    pass
for i in range(8):
    a &= ~(1 << i)
    print(f"{a:b}")