"""
hall
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
sits numbers
             9876543210

cell ticket
check sit
return ticket
print sits in hall
empty hall

"""

ROWS_NUMBER = 10
SITS = 20
cinema_hall = [ 1 << SITS for i in range(ROWS_NUMBER)]

# print (F"{~0xFFFFFF:b}")

print ()

def print_all_sits(hall): 
    # print sits N
    print (F"Sit numbers ->\t", end="")
    for i in reversed(range(SITS)):
        print (F"{(i+1):<3d}", end="")
        pass
    print()
    print()

    for row_number in range(len(hall)):
        sits =  F"{hall[row_number]:b}"
        print (F"Row: {(ROWS_NUMBER - row_number):4d}\t", end="")
        for i in range(1,len(sits)):
            print (F"{sits[i]:3s}", end="")
            pass
        print()
    pass

print_all_sits(cinema_hall)
cinema_hall[2] = 0b1111111111111111

def check_sit(r: int, s: int, hall: list) -> bool: return (hall[ROWS_NUMBER-r] >> (s-1)) & 1
def sell_ticket(r: int, s: int, hall: list) -> bool: hall[ROWS_NUMBER-r] |= 1 << (s-1)
    
print (check_sit( 1, 2, cinema_hall))
print (check_sit( 1, 2, cinema_hall))
sell_ticket( 1, 2, cinema_hall)
print_all_sits(cinema_hall)