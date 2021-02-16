# Tic Tae Toe Project

box = [" ", " ", " ",
       " ", " ", " ", 
       " ", " ", " "]

play_game = True

def main():

    while True:
        prompt1 = input("Do you want to play? (Y/N): ").upper()
        if prompt1 == "Y":
            start_game()
        elif prompt1 == "N":
            print("Have a nice day!")
            break
        
    return

def start_game():

    global player1
    global player2

    prompt2 = input("Player1: Pick a side. (X/O): ").upper()
    if prompt2 == "X":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"

    show_board()
    player_turn = player1
    game_still_going = True

    while game_still_going == True:
        move = player_enter_move(player_turn)
        box[move-1] = player_turn
        show_board()
        if check_game_still_going() == False:
            break
        if player_turn == player1:
            player_turn = player2
        else:
            player_turn = player1
    
    winner = player_turn
    print("Congrats " + winner + "!!!")

    return

def show_board():
    
    row1 = box[0] + "|" + box[1] + "|" + box[2]
    row2 = box[3] + "|" + box[4] + "|" + box[5]
    row3 = box[6] + "|" + box[7] + "|" + box[8]

    print(row1)
    print(row2)
    print(row3)

    return

def player_enter_move(i):
    while True:
        if i == player1:
            move = int(input("Player 1's turn. Pick a spot from 1-9: "))
            if box[move-1] == " ":
                break
        else:
            move = int(input("Player 2's turn. Pick a spot from 1-9: "))
            if box[move-1] == " ":
                break
    return move

def check_game_still_going():
    if box[0] == box[1] == box[2] != " " or box[3] == box[4] == box[5] != " " or box[6] == box[7] == box[8] != " ":
        return False
    elif box[0] == box[3] == box[6] != " " or box[1] == box[4] == box[7] != " " or box[2] == box[5] == box[8] != " ":
        return False
    elif box[0] == box[4] == box[8] != " " or box[2] == box[4] == box[6] != " ":
        return False
    else:
        return True

main()