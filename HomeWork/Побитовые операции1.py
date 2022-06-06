# https://www.youtube.com/watch?v=nwBKiIx3gsE

a = 0b0101
b = 0b1010

print(f"{a:b}")
print(f"{b:b}")
c = a & b
print(f" c = a & b: {c:b}")
c = a | b
print(f" c = a | b: {c:b}")
c = a ^ b
print(f" c = a ^ b: {c:b}")
c = ~c
print(f" c = ~c: {c:b}")

d = 15
d = ~d + 1 # 15
print(f" d = ~d: {d}") # 15