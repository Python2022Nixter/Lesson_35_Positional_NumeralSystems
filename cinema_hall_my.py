"""
hall 
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000

 cell ticket
 check sit
 return ticket
 print sits in hall
"""

ROWS_NUMBER = 10
SITS = 5

cinema_hall = [ 1 << SITS for i in range(ROWS_NUMBER)]
# print(F"{~0xFFFFF:b}")

print()
def print_all_sits(hall):
    for row in hall:
        print(F"{row:b}")
print_all_sits(cinema_hall)

# def check sit (row, column):
def check_sit( row, column):
    if row < 0 or row >= ROWS_NUMBER:
        return False
    if column < 0 or column >= SITS:
        return False
    return (cinema_hall[row] & (1 << column)) == 0

print(check_sit( 0, 0))
print(check_sit( 0, 4))

# def cell ticket (row, column):
def cell_ticket( row, column):
    if check_sit( row, column):
        cinema_hall[row] |= 1 << column
        return True

cell_ticket( 0, 4)
print_all_sits(cinema_hall)