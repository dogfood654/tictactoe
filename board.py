# 1. Have the user define X for an x by x board. Meaning support anything from 3x3 to 10x10 boards dynamically based on user input.

board_size = int(input("Size of board: "))
print(str(board_size) + " x " + str(board_size))
total = board_size * board_size

d = {}
# create a dictionary storing all the values
for i in range(1,total+1):
    d["string{0}".format(i)] = " "

# print dictionary
for i in range(1, total+1):
    if i % board_size == 0:
        print(" ")
    else:
        print(d["string{0}".format(i)], end = "")
        print("|", end = "")
        