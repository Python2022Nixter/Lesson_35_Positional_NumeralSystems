# https://www.youtube.com/watch?v=myW_9B9T_II

# ~ 


a = 121 
print(bin(a), a)
a = ~a + 1
print(bin(a), a)

# & - Амерсанд,  оператор побитового И
flags = 5
mask = 4
res = flags & mask
print(f"{flags:b} & {mask:b} = {res:b}, {flags} & {mask} = {res}")

if flags & mask == mask:
    print("2-й бит включен")
else:
    print("2-й бит выключен")
    
