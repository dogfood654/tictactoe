def main():
    global player_turn

    # Settings
    ask_board_size()
    create_boxes()
    ask_consecutive()
    pick_shape()

    # Start game
    display_board()
    player_turn = player1
    box_filled = 0

    while True:
        move = player_enter_move(player_turn)
        d["string{0}".format(move)] = player_turn
        display_board()
        if check() == True:
            break
        player_turn = switch_turn(player_turn)
        box_filled += 1
        if box_filled == total:
            break

    if check() == True:
        print("Player " + player_turn + " wins!")
    else:
        print("Draw!")

    return

def ask_board_size():
    global board_size
    global total
    board_size = 0
    total = 0

    while True:
        try:
            board_size = int(input("Size of board: "))
            assert(board_size > 1)
            break
        except:
            print("Please enter an integer which is greater than 1.")
    total = board_size * board_size
    return

def create_boxes():
    global d
    d = {}

    for i in range(1,total+1):
        d["string{0}".format(i)] = " "
    return

def ask_consecutive():
    global consecutive
    consecutive = 0

    while True:
        try:
            consecutive = int(input("How many in a row to win? "))
            assert(consecutive > 1)
            break
        except:
            print("Please enter an integer which is greater than 1.")
    return        

def pick_shape():
    global player1
    global player2

    prompt1 = ""
    while prompt1 != "X" or "O":
        if prompt1 == "X":
            player1 = "X"
            player2 = "O"
            break
        elif prompt1 == "O":
            player1 = "O"
            player2 = "X"
            break
        else:
            prompt1 = input("Player1: Pick a side. (X/O): ").upper()
    return

def display_board():
    for i in range(1, total+1):
        if i % board_size == 0:
            print(d["string{0}".format(i)])
        else:
            print(d["string{0}".format(i)], end = "")
            print("|", end = "")
    return

def player_enter_move(i):
    while True:
        try:
            move = int(input("Player " + player_turn + "'s turn. Pick a spot from 1-9: "))
            assert(move <= total)
            assert(move >= 1)
            if d["string{0}".format(move)] == " ":
                break
        except:
            print("Please enter a valid spot.")
    return move

def switch_turn(i):
    if i == player1:
        i = player2
    else:
        i = player1
    return i

def check():
    boo1 = check_horizontal()
    boo2 = check_vertical()
    boo3 = check_diagonal1()
    boo4 = check_diagonal2()
    boo5 = check_diagonal3()
    boo6 = check_diagonal4()

    if boo1 or boo2 or boo3 or boo4 or boo5  or boo6 == True:
        return True
    else:
        return False

def check_horizontal():
    global in_a_row
    in_a_row = 0

    for i in range(1,total+1):
        if i % board_size == 1:
            in_a_row = 0
        if d["string{0}".format(i)] == player_turn:
            in_a_row += 1
        else:
            in_a_row = 0
        if in_a_row == consecutive:
            break
        if i % board_size == 0:
            if in_a_row == consecutive:
                break
    
    boo = check_in_a_row()
    return boo

def check_vertical():
    global in_a_row

    for i in range(1,board_size+1):
        in_a_row = 0
        y = i
        for x in range(0,board_size):
            z = y + (x * board_size)
            if d["string{0}".format(z)] == player_turn:
                in_a_row += 1
            else:
                in_a_row = 0
            if in_a_row == consecutive:
                break
            if x == board_size-1:
                if in_a_row == consecutive:
                    break
        if in_a_row == consecutive:
            break

    boo = check_in_a_row()
    return boo

def check_diagonal1():
    global in_a_row

    for i in range(1,board_size+1):
        in_a_row = 0
        y = i
        for x in range(0,board_size):
            z = y + x * (board_size + 1)
            if d["string{0}".format(z)] == player_turn:
                in_a_row += 1
            else:
                in_a_row = 0
            if in_a_row == consecutive:
                break
            if x == board_size-1:
                if in_a_row == consecutive:
                    break
            if z % board_size == 0:
                break
        if in_a_row == consecutive:
            break

    boo = check_in_a_row()
    return boo    

def check_diagonal2():
    global in_a_row

    list1 = []
    number = board_size
    for i in range(1, number*number, board_size):
        list1.append(i)

    for i in range(0,board_size):
        in_a_row = 0
        y = list1[i]
        for x in range(0,board_size):
            z = y + x * (board_size + 1)
            if d["string{0}".format(z)] == player_turn:
                in_a_row += 1
            else:
                in_a_row = 0
            if in_a_row == consecutive:
                break
            if x == board_size-1:
                if in_a_row == consecutive:
                    break
            if z >= (total - board_size + 1):
                break
        if in_a_row == consecutive:
            break

    boo = check_in_a_row()
    return boo   

def check_diagonal3():
    global in_a_row

    for i in range(1,board_size+1):
        in_a_row = 0
        y = i
        for x in range(0,board_size):
            z = y + x * (board_size-1)
            if d["string{0}".format(z)] == player_turn:
                in_a_row += 1
            else:
                in_a_row = 0
            if in_a_row == consecutive:
                break
            if x == board_size-1:
                if in_a_row == consecutive:
                    break
            if z % board_size == 1:
                break
        if in_a_row == consecutive:
            break

    boo = check_in_a_row()
    return boo   

def check_diagonal4():
    global in_a_row

    list2 = []
    number = board_size
    for i in range(number, number*number+1, board_size):
        list2.append(i)

    for i in range(0,board_size):
        in_a_row = 0
        y = list2[i]
        for x in range(0,board_size):
            z = y + x * (board_size-1)
            if d["string{0}".format(z)] == player_turn:
                in_a_row += 1
            else:
                in_a_row = 0
            if in_a_row == consecutive:
                break
            if x == board_size-1:
                if in_a_row == consecutive:
                    break
            if z >= (total - board_size + 1):
                break
        if in_a_row == consecutive:
            break

    boo = check_in_a_row()
    return boo   

def check_in_a_row():
    if in_a_row == consecutive:
        return True
    else:
        return False

main()